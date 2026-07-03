/* ============================================================
   KrishiKonnect Service Worker  —  sw.js
   Place this file in your PROJECT ROOT (same level as index.html)
   ============================================================ */

const CACHE_VERSION   = 'v1';
const STATIC_CACHE    = `krishikonnect-static-${CACHE_VERSION}`;
const DYNAMIC_CACHE   = `krishikonnect-dynamic-${CACHE_VERSION}`;
const OFFLINE_PAGE    = '/offline.html';

/* Files to cache immediately on install */
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/pwa.css',
  '/icons/icon-72.png',
  '/icons/icon-96.png',
  '/icons/icon-192.png',
  '/icons/icon-512.png',
  OFFLINE_PAGE
];

/* ── INSTALL ── cache all static assets ── */
self.addEventListener('install', event => {
  console.log('[SW] Installing KrishiKonnect service worker...');
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(cache => {
        console.log('[SW] Caching static assets');
        return cache.addAll(STATIC_ASSETS);
      })
      .then(() => self.skipWaiting())
      .catch(err => console.warn('[SW] Cache install error:', err))
  );
});

/* ── ACTIVATE ── delete old caches ── */
self.addEventListener('activate', event => {
  console.log('[SW] Activating...');
  const allowedCaches = [STATIC_CACHE, DYNAMIC_CACHE];
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys
          .filter(key => !allowedCaches.includes(key))
          .map(key => {
            console.log('[SW] Deleting old cache:', key);
            return caches.delete(key);
          })
      ))
      .then(() => self.clients.claim())
  );
});

/* ── FETCH ── stale-while-revalidate strategy ── */
self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  /* Skip non-GET requests and browser-extension / chrome-extension URLs */
  if (request.method !== 'GET') return;
  if (!url.protocol.startsWith('http')) return;

  /* ── API calls — network first, no cache ── */
  if (
    url.hostname.includes('anthropic.com') ||
    url.hostname.includes('generativelanguage') ||
    url.hostname.includes('openai.com') ||
    url.pathname.includes('/api/')
  ) {
    event.respondWith(
      fetch(request).catch(() => new Response(
        JSON.stringify({ error: 'You are offline. Please reconnect to use AI features.' }),
        { headers: { 'Content-Type': 'application/json' } }
      ))
    );
    return;
  }

  /* ── Navigation requests — serve app shell, fallback to offline page ── */
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(response => {
          const clone = response.clone();
          caches.open(DYNAMIC_CACHE).then(cache => cache.put(request, clone));
          return response;
        })
        .catch(() =>
          caches.match('/index.html')
            .then(cached => cached || caches.match(OFFLINE_PAGE))
        )
    );
    return;
  }

  /* ── All other requests — cache first, then network ── */
  event.respondWith(
    caches.match(request)
      .then(cached => {
        const fetchPromise = fetch(request).then(networkResponse => {
          if (networkResponse && networkResponse.status === 200) {
            caches.open(DYNAMIC_CACHE)
              .then(cache => cache.put(request, networkResponse.clone()));
          }
          return networkResponse;
        }).catch(() => cached);

        return cached || fetchPromise;
      })
  );
});

/* ── BACKGROUND SYNC — retry failed report submissions ── */
self.addEventListener('sync', event => {
  if (event.tag === 'sync-reports') {
    console.log('[SW] Background sync: retrying pending reports...');
    event.waitUntil(syncPendingReports());
  }
});

async function syncPendingReports() {
  /* Placeholder — wire up to your IndexedDB queue if needed */
  console.log('[SW] syncPendingReports: no pending items.');
}

/* ── PUSH NOTIFICATIONS (optional, for future use) ── */
self.addEventListener('push', event => {
  if (!event.data) return;
  const data = event.data.json();
  self.registration.showNotification(data.title || 'KrishiKonnect', {
    body:    data.body    || 'New update from KrishiKonnect',
    icon:    '/icons/icon-192.png',
    badge:   '/icons/icon-96.png',
    tag:     'krishi-notification',
    renotify: true
  });
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  event.waitUntil(
    clients.openWindow('/')
  );
});

console.log('[SW] KrishiKonnect service worker loaded.');