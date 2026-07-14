const CACHE_VERSION   = 'v2';
const STATIC_CACHE    = `krishikonnect-static-${CACHE_VERSION}`;
const DYNAMIC_CACHE   = `krishikonnect-dynamic-${CACHE_VERSION}`;
const OFFLINE_PAGE    = '/offline.html';

/* Files to cache — icons now at ROOT level, no icons/ subfolder */
const STATIC_ASSETS = [
  '/',
  '/index.html',
  '/manifest.json',
  '/style.css',
  '/pwa.css',
  '/icon-192.png',
  '/icon-512.png',
  OFFLINE_PAGE
];

self.addEventListener('install', event => {
  event.waitUntil(
    caches.open(STATIC_CACHE)
      .then(cache => cache.addAll(STATIC_ASSETS))
      .then(() => self.skipWaiting())
      .catch(err => console.warn('[SW] Cache install error:', err))
  );
});

self.addEventListener('activate', event => {
  const allowed = [STATIC_CACHE, DYNAMIC_CACHE];
  event.waitUntil(
    caches.keys()
      .then(keys => Promise.all(
        keys.filter(k => !allowed.includes(k)).map(k => caches.delete(k))
      ))
      .then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const { request } = event;
  const url = new URL(request.url);

  if (request.method !== 'GET') return;
  if (!url.protocol.startsWith('http')) return;

  /* API calls — network only */
  if (
    url.hostname.includes('anthropic.com') ||
    url.hostname.includes('generativelanguage') ||
    url.pathname.includes('/api/')
  ) {
    event.respondWith(
      fetch(request).catch(() => new Response(
        JSON.stringify({ error: 'Offline — AI features unavailable.' }),
        { headers: { 'Content-Type': 'application/json' } }
      ))
    );
    return;
  }

  /* Navigation — serve index.html, fallback to offline */
  if (request.mode === 'navigate') {
    event.respondWith(
      fetch(request)
        .then(res => {
          caches.open(DYNAMIC_CACHE).then(c => c.put(request, res.clone()));
          return res;
        })
        .catch(() => caches.match('/index.html').then(c => c || caches.match(OFFLINE_PAGE)))
    );
    return;
  }

  /* Everything else — cache first */
  event.respondWith(
    caches.match(request).then(cached => {
      const network = fetch(request).then(res => {
        if (res && res.status === 200)
          caches.open(DYNAMIC_CACHE).then(c => c.put(request, res.clone()));
        return res;
      }).catch(() => cached);
      return cached || network;
    })
  );
});

self.addEventListener('push', event => {
  if (!event.data) return;
  const data = event.data.json();
  self.registration.showNotification(data.title || 'KrishiKonnect', {
    body: data.body || 'New update from KrishiKonnect',
    icon: '/icon-192.png',
    badge: '/icon-96.png',
    tag: 'krishi-notification',
    renotify: true
  });
});

self.addEventListener('notificationclick', event => {
  event.notification.close();
  event.waitUntil(clients.openWindow('/'));
});