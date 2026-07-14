"""
KrishiKonnect — Knowledge Base
ICAR-aligned disease profiles, regional agro-climate data,
mandi price references, and AI agent prompts.
"""

# ═══════════════════════════════════════════════════════════════
# DISEASE PROFILES  (ICAR-referenced)
# ═══════════════════════════════════════════════════════════════

DISEASE_PROFILES = {
    # ── TOMATO ────────────────────────────────────────────────
    "early_blight": {
        "name": "Early Blight (Alternaria solani)",
        "crop": "Tomato",
        "pathogen": "Alternaria solani",
        "class": "Fungal",
        "severity": "HIGH",
        "symptoms": ["concentric brown rings", "yellow halo", "target board pattern", "lower leaf progression"],
        "conditions": ["warm humid", "25-30°C", "leaf wetness"],
        "chemical_rx": {
            "primary": "Mancozeb 75 WP @ 2 g/L + Azoxystrobin 23 SC @ 1 mL/L, spray every 7 days × 3 cycles",
            "alternate": "Chlorothalonil 75 WP @ 2 g/L",
            "preharvest_interval": "14 days"
        },
        "bio_rx": {
            "primary": "Trichoderma viride @ 4 g/L soil drench + Pseudomonas fluorescens @ 10 mL/L foliar spray",
            "notes": "Apply at 10-day intervals"
        },
        "ipm": [
            "Remove and destroy infected lower leaves immediately",
            "Avoid overhead irrigation; switch to drip",
            "Maintain plant spacing ≥ 60 cm for airflow",
            "Apply mulch to reduce soil splash",
            "Rotate with non-solanaceous crops for 2 seasons"
        ],
        "economic_threshold": "5% defoliation or 3 lesions per leaf",
        "decay_rate": 0.12,
        "recovery_k": 0.28,
        "confidence_base": 0.87
    },
    "late_blight": {
        "name": "Late Blight (Phytophthora infestans)",
        "crop": "Tomato",
        "pathogen": "Phytophthora infestans",
        "class": "Oomycete",
        "severity": "CRITICAL",
        "symptoms": ["water-soaked lesions", "white mycelium underside", "brown greasy patches", "rapid collapse"],
        "conditions": ["cool wet", "15-20°C", "high humidity >90%"],
        "chemical_rx": {
            "primary": "Metalaxyl-M + Mancozeb (Ridomil Gold) @ 2.5 g/L, spray every 5–7 days",
            "alternate": "Cymoxanil 8% + Mancozeb 64% WP @ 3 g/L",
            "preharvest_interval": "7 days"
        },
        "bio_rx": {
            "primary": "Bacillus subtilis (Serenade) @ 2 g/L, spray preventively",
            "notes": "Not curative — use as part of IPM rotation"
        },
        "ipm": [
            "Monitor weather — apply protectants before rains",
            "Remove infected plants entirely and burn",
            "Avoid excess nitrogen fertilization",
            "Use resistant varieties: ICAR-TH-1, Arka Rakshak"
        ],
        "economic_threshold": "Any confirmed detection — act immediately",
        "decay_rate": 0.20,
        "recovery_k": 0.22,
        "confidence_base": 0.91
    },
    "bacterial_wilt": {
        "name": "Bacterial Wilt (Ralstonia solanacearum)",
        "crop": "Tomato",
        "pathogen": "Ralstonia solanacearum",
        "class": "Bacterial",
        "severity": "HIGH",
        "symptoms": ["sudden wilt without yellowing", "vascular browning", "milky ooze in water test", "rapid collapse"],
        "conditions": ["warm tropical", "soil temp >25°C", "water-logged soil"],
        "chemical_rx": {
            "primary": "No curative chemical. Bordeaux mixture 1% as preventive soil drench",
            "alternate": "Streptocycline 200 ppm spray (early stage only)",
            "preharvest_interval": "N/A"
        },
        "bio_rx": {
            "primary": "Bacillus subtilis + Trichoderma harzianum soil application @ 5 g/kg soil",
            "notes": "Biocontrol most effective as preventive"
        },
        "ipm": [
            "Remove and destroy wilted plants including roots",
            "Do not replant solanaceous crops for 3+ seasons",
            "Improve drainage; avoid waterlogging",
            "Solarize soil with polythene for 4–6 weeks",
            "Use grafted plants on Solanum torvum rootstock"
        ],
        "economic_threshold": "Any confirmed case — no recovery possible",
        "decay_rate": 0.18,
        "recovery_k": 0.15,
        "confidence_base": 0.83
    },

    # ── WHEAT ─────────────────────────────────────────────────
    "stripe_rust": {
        "name": "Yellow/Stripe Rust (Puccinia striiformis)",
        "crop": "Wheat",
        "pathogen": "Puccinia striiformis f.sp. tritici",
        "class": "Fungal",
        "severity": "HIGH",
        "symptoms": ["linear yellow pustules on leaves", "stripe pattern parallel to veins", "urediniospore deposits", "sheath infection"],
        "conditions": ["cool humid", "10-15°C", "dew or light rain"],
        "chemical_rx": {
            "primary": "Propiconazole 25 EC @ 1 mL/L, spray at flag leaf stage",
            "alternate": "Tebuconazole 25.9 EC @ 1 mL/L",
            "preharvest_interval": "21 days"
        },
        "bio_rx": {
            "primary": "5% NSKE (Neem Seed Kernel Extract) spray @ 10-day intervals",
            "notes": "Suppressive not curative"
        },
        "ipm": [
            "Sow resistant varieties: DBW-222, HD-3086, PBW-502",
            "Timely sowing — avoid very early or late sowing",
            "Balanced NPK — avoid excess nitrogen",
            "Monitor from tillering stage weekly"
        ],
        "economic_threshold": "5% leaf area infected at any growth stage",
        "decay_rate": 0.10,
        "recovery_k": 0.30,
        "confidence_base": 0.89
    },
    "powdery_mildew_wheat": {
        "name": "Powdery Mildew (Blumeria graminis)",
        "crop": "Wheat",
        "pathogen": "Blumeria graminis f.sp. tritici",
        "class": "Fungal",
        "severity": "MEDIUM",
        "symptoms": ["white powdery colonies on leaves", "yellowing below patches", "stem and ear infection"],
        "conditions": ["cool dry to moderately humid", "15-20°C"],
        "chemical_rx": {
            "primary": "Triadimefon 25 WP @ 1 g/L or Propiconazole 25 EC @ 1 mL/L",
            "alternate": "Sulphur 80 WP @ 3 g/L",
            "preharvest_interval": "14 days"
        },
        "bio_rx": {
            "primary": "Ampelomyces quisqualis based biocontrol @ label rate",
            "notes": "Apply early in disease cycle"
        },
        "ipm": [
            "Use resistant varieties",
            "Avoid dense canopy through proper spacing",
            "Reduce nitrogen application rates"
        ],
        "economic_threshold": "10% leaf area at boot stage",
        "decay_rate": 0.07,
        "recovery_k": 0.32,
        "confidence_base": 0.82
    },

    # ── RICE ──────────────────────────────────────────────────
    "rice_blast": {
        "name": "Rice Blast (Magnaporthe oryzae)",
        "crop": "Rice",
        "pathogen": "Magnaporthe oryzae",
        "class": "Fungal",
        "severity": "HIGH",
        "symptoms": ["spindle-shaped grey lesions", "brown borders", "lesions coalescing", "neck blast at panicle"],
        "conditions": ["moderate temperature 24-28°C", "high humidity", "heavy dew"],
        "chemical_rx": {
            "primary": "Tricyclazole 75 WP @ 0.6 g/L, spray at tillering and panicle initiation",
            "alternate": "Carbendazim 50 WP @ 1 g/L or Isoprothiolane 40 EC @ 1.5 mL/L",
            "preharvest_interval": "14 days"
        },
        "bio_rx": {
            "primary": "Pseudomonas fluorescens @ 10 mL/L foliar spray",
            "notes": "Seed treatment with Trichoderma also effective"
        },
        "ipm": [
            "Use blast-resistant varieties: MTU-1010, IR-64, BPT-5204",
            "Avoid excess nitrogen — split urea application",
            "Maintain 2–3 cm water level during tillering",
            "Remove and burn diseased stubble after harvest"
        ],
        "economic_threshold": "Leaf blast: 2% leaf area; neck blast: any infection",
        "decay_rate": 0.09,
        "recovery_k": 0.22,
        "confidence_base": 0.85
    },
    "bacterial_leaf_blight": {
        "name": "Bacterial Leaf Blight (Xanthomonas oryzae)",
        "crop": "Rice",
        "pathogen": "Xanthomonas oryzae pv. oryzae",
        "class": "Bacterial",
        "severity": "HIGH",
        "symptoms": ["water-soaked margins", "yellow to straw-colored leaf blight", "wilting of young leaves (kresek)"],
        "conditions": ["flood water", "warm >30°C", "cyclone/storm conditions"],
        "chemical_rx": {
            "primary": "Streptocycline @ 100 ppm + Copper oxychloride 50 WP @ 2 g/L",
            "alternate": "Copper hydroxide @ 2 g/L",
            "preharvest_interval": "21 days"
        },
        "bio_rx": {
            "primary": "Pseudomonas fluorescens @ 10 mL/L spray at 30 and 50 DAS",
            "notes": "Biocontrol agents have moderate efficacy only"
        },
        "ipm": [
            "Use resistant varieties: Pusa Basmati-1, IR-36",
            "Drain flooded fields promptly",
            "Avoid high nitrogen fertilization",
            "Do not use flood water from infected areas for irrigation"
        ],
        "economic_threshold": "10% leaf area affected",
        "decay_rate": 0.11,
        "recovery_k": 0.24,
        "confidence_base": 0.80
    },

    # ── COTTON ────────────────────────────────────────────────
    "cotton_bollworm": {
        "name": "American Bollworm (Helicoverpa armigera)",
        "crop": "Cotton",
        "pathogen": "Helicoverpa armigera (insect)",
        "class": "Insect Pest",
        "severity": "HIGH",
        "symptoms": ["shot-hole feeding on squares", "boll damage with frass", "larval entry holes", "premature shedding"],
        "conditions": ["dry hot conditions", "April-October"],
        "chemical_rx": {
            "primary": "Emamectin benzoate 5 SG @ 0.5 g/L or Spinosad 45 SC @ 0.3 mL/L",
            "alternate": "Chlorantraniliprole 18.5 SC @ 0.3 mL/L",
            "preharvest_interval": "14 days"
        },
        "bio_rx": {
            "primary": "NPV (Nuclear Polyhedrosis Virus) @ 250 LE/ha; Bt (Bacillus thuringiensis) @ 1 kg/ha",
            "notes": "Apply at early instar stage for best effect"
        },
        "ipm": [
            "Install pheromone traps @ 5/ha; threshold 2 moths/trap/night",
            "Hand-pick egg masses and early instars",
            "Grow Bt cotton to reduce chemical use",
            "Inter-crop with maize or sorghum as trap crop"
        ],
        "economic_threshold": "5% damage on bolls or 2 larvae per plant",
        "decay_rate": 0.13,
        "recovery_k": 0.25,
        "confidence_base": 0.78
    },
    "powdery_mildew_cotton": {
        "name": "Powdery Mildew (Leveillula taurica)",
        "crop": "Cotton",
        "pathogen": "Leveillula taurica",
        "class": "Fungal",
        "severity": "MEDIUM",
        "symptoms": ["white powdery coating on upper leaf surface", "leaf curl", "premature drop"],
        "conditions": ["dry hot days", "cool nights", "low humidity"],
        "chemical_rx": {
            "primary": "Dinocap 48 EC @ 1 mL/L or Hexaconazole 5 SC @ 2 mL/L",
            "alternate": "Sulphur 80 WP @ 3 g/L",
            "preharvest_interval": "14 days"
        },
        "bio_rx": {
            "primary": "Trichoderma viride @ 4 g/L spray",
            "notes": ""
        },
        "ipm": [
            "Remove and destroy severely infected leaves",
            "Maintain optimal plant density",
            "Avoid excess potassium deficiency — apply balanced fertilizer"
        ],
        "economic_threshold": "20% leaf area infected",
        "decay_rate": 0.06,
        "recovery_k": 0.30,
        "confidence_base": 0.76
    },

    # ── POTATO ────────────────────────────────────────────────
    "potato_late_blight": {
        "name": "Potato Late Blight (Phytophthora infestans)",
        "crop": "Potato",
        "pathogen": "Phytophthora infestans",
        "class": "Oomycete",
        "severity": "CRITICAL",
        "symptoms": ["water-soaked dark brown lesions on leaf margins", "white mycelium underside", "tubers show internal browning", "rapid necrosis"],
        "conditions": ["cool wet", "10-18°C", "humidity >90%"],
        "chemical_rx": {
            "primary": "Metalaxyl-M 4% + Mancozeb 64% WP @ 2.5 g/L every 5–7 days",
            "alternate": "Cymoxanil 8% + Mancozeb 64% WP @ 3 g/L",
            "preharvest_interval": "10 days"
        },
        "bio_rx": {
            "primary": "Bacillus subtilis @ 2 g/L as preventive spray",
            "notes": "Begin at tuber initiation stage"
        },
        "ipm": [
            "Use certified disease-free seed tubers",
            "Hilling up to protect tubers from sporangia wash",
            "Maintain wide row spacing for airflow",
            "Apply preventively before rains during cool season"
        ],
        "economic_threshold": "Any confirmed lesion — act same day",
        "decay_rate": 0.18,
        "recovery_k": 0.20,
        "confidence_base": 0.88
    },

    # ── MAIZE ─────────────────────────────────────────────────
    "maize_fall_armyworm": {
        "name": "Fall Armyworm (Spodoptera frugiperda)",
        "crop": "Maize",
        "pathogen": "Spodoptera frugiperda (insect)",
        "class": "Insect Pest",
        "severity": "HIGH",
        "symptoms": ["window-pane feeding", "ragged holes in whorls", "frass in whorl", "multiple entry holes"],
        "conditions": ["warm tropical", "May-September"],
        "chemical_rx": {
            "primary": "Emamectin benzoate 5 SG @ 0.5 g/L or Chlorantraniliprole 18.5 SC @ 0.4 mL/L into whorl",
            "alternate": "Spinetoram 11.7 SC @ 0.5 mL/L",
            "preharvest_interval": "14 days"
        },
        "bio_rx": {
            "primary": "Bt (Bacillus thuringiensis var. kurstaki) @ 1 kg/ha; Beauveria bassiana @ 5 g/L",
            "notes": "Apply into whorl in evening hours"
        },
        "ipm": [
            "Release Trichogramma chilonis egg parasitoids @ 50,000/ha",
            "Apply sand + lime 9:1 into whorl as physical barrier",
            "Use pheromone traps for monitoring",
            "Early sowing to escape peak infestation"
        ],
        "economic_threshold": "10% plants showing fresh damage",
        "decay_rate": 0.11,
        "recovery_k": 0.26,
        "confidence_base": 0.82
    },

    # ── CHILI ─────────────────────────────────────────────────
    "chili_anthracnose": {
        "name": "Anthracnose / Dieback (Colletotrichum capsici)",
        "crop": "Chili",
        "pathogen": "Colletotrichum capsici",
        "class": "Fungal",
        "severity": "HIGH",
        "symptoms": ["circular sunken lesions on fruits", "concentric rings", "dieback of shoots", "seed infection"],
        "conditions": ["warm humid", "25-30°C", "rain splash"],
        "chemical_rx": {
            "primary": "Carbendazim 50 WP @ 1 g/L + Mancozeb 75 WP @ 2 g/L, spray every 10 days",
            "alternate": "Azoxystrobin 23 SC @ 1 mL/L",
            "preharvest_interval": "7 days"
        },
        "bio_rx": {
            "primary": "Trichoderma harzianum @ 4 g/L foliar spray",
            "notes": "Seed treatment with Carbendazim 2g/kg critical"
        },
        "ipm": [
            "Hot water seed treatment at 52°C for 30 min",
            "Collect and destroy fallen fruits daily",
            "Provide good drainage and avoid dense planting"
        ],
        "economic_threshold": "5% fruit damage",
        "decay_rate": 0.10,
        "recovery_k": 0.27,
        "confidence_base": 0.80
    },

    # ── GENERAL / ABIOTIC ─────────────────────────────────────
    "abiotic_stress": {
        "name": "Abiotic / Nutritional Stress",
        "crop": "General",
        "pathogen": "Non-pathogenic",
        "class": "Abiotic",
        "severity": "LOW",
        "symptoms": ["interveinal chlorosis", "tip burn", "stunted growth", "purpling", "edge necrosis"],
        "conditions": ["nutrient deficiency", "drought", "waterlogging", "pH imbalance"],
        "chemical_rx": {
            "primary": "Conduct soil and tissue test first. Apply balanced NPK based on report.",
            "alternate": "Micronutrient foliar spray: 0.5% ZnSO4 + 0.1% Borax for zinc/boron deficiency",
            "preharvest_interval": "N/A"
        },
        "bio_rx": {
            "primary": "Vermicompost @ 2 t/ha + Bacillus subtilis soil drench",
            "notes": "Improve soil organic matter and microbiome"
        },
        "ipm": [
            "Soil test every 3 years — submit to local KVK",
            "Check irrigation water EC and pH",
            "Apply organic matter annually",
            "Check for root damage from nematodes"
        ],
        "economic_threshold": "Variable — consult soil health card",
        "decay_rate": 0.05,
        "recovery_k": 0.20,
        "confidence_base": 0.65
    },
}

# ═══════════════════════════════════════════════════════════════
# REGIONAL AGRO-CLIMATE PROFILES
# ═══════════════════════════════════════════════════════════════

REGIONAL_PROFILES = {
    "Punjab (Alluvial Plains)": {
        "soil": "Deep alluvial loam, high organic matter",
        "rainfall": "500–700 mm, monsoon July–September",
        "temperature": "Summer 35–45°C, Winter 2–10°C",
        "major_crops": ["Wheat", "Rice (Basmati)", "Maize", "Potato", "Cotton"],
        "disease_pressure": {"stripe_rust": "HIGH", "bacterial_leaf_blight": "MEDIUM", "powdery_mildew_wheat": "MEDIUM"},
        "risk_season": "October–March (Rabi diseases); July–August (Kharif pests)",
        "water_table": "Shallow — 3–8 m, waterlogging risk",
        "icar_kvk": "PAU Ludhiana; KVK Amritsar"
    },
    "Haryana (Semi-Arid)": {
        "soil": "Sandy loam to clay loam, moderate fertility",
        "rainfall": "300–600 mm",
        "temperature": "Summer 40–48°C, Winter 3–15°C",
        "major_crops": ["Wheat", "Rice", "Cotton", "Mustard", "Sugarcane"],
        "disease_pressure": {"stripe_rust": "HIGH", "cotton_bollworm": "HIGH", "powdery_mildew_wheat": "MEDIUM"},
        "risk_season": "November–February (rust); June–September (bollworm)",
        "water_table": "Declining — over-extraction concern",
        "icar_kvk": "CCS HAU Hisar; KVK Karnal"
    },
    "Uttar Pradesh (Gangetic Plains)": {
        "soil": "Alluvial, heavy calcareous, moderate-high fertility",
        "rainfall": "700–1000 mm",
        "temperature": "Summer 38–44°C, Winter 5–18°C",
        "major_crops": ["Wheat", "Rice", "Sugarcane", "Potato", "Maize"],
        "disease_pressure": {"stripe_rust": "HIGH", "rice_blast": "MEDIUM", "potato_late_blight": "HIGH"},
        "risk_season": "Jan–Feb (rust); July–Sept (rice blast); Oct–Dec (potato blight)",
        "water_table": "Variable 5–20 m",
        "icar_kvk": "IARI New Delhi outreach; KVK Lucknow, Kanpur"
    },
    "Maharashtra (Deccan Plateau)": {
        "soil": "Black cotton soil (Vertisol), high clay, high water retention",
        "rainfall": "600–1400 mm (highly variable)",
        "temperature": "Summer 35–42°C, Winter 15–28°C",
        "major_crops": ["Cotton", "Sugarcane", "Soybean", "Onion", "Tomato", "Jowar"],
        "disease_pressure": {"powdery_mildew_cotton": "HIGH", "cotton_bollworm": "HIGH", "early_blight": "MEDIUM"},
        "risk_season": "June–October (Kharif pests); March–May (dry season diseases)",
        "water_table": "Deep 30–60 m on plateau",
        "icar_kvk": "VNMKV Parbhani; KVK Nashik, Pune"
    },
    "Karnataka (Red Lateritic)": {
        "soil": "Red laterite, low organic matter, good drainage",
        "rainfall": "700–1500 mm",
        "temperature": "Mild 20–32°C year-round",
        "major_crops": ["Rice", "Maize", "Tomato", "Cotton", "Sunflower", "Ragi"],
        "disease_pressure": {"early_blight": "HIGH", "bacterial_wilt": "HIGH", "rice_blast": "MEDIUM", "maize_fall_armyworm": "HIGH"},
        "risk_season": "July–November (blight season); May–August (fall armyworm)",
        "water_table": "Variable 10–40 m",
        "icar_kvk": "UAS Bengaluru; KVK Dharwad, Raichur"
    },
    "Tamil Nadu (Cauvery Delta)": {
        "soil": "Clay loam alluvial in delta, red laterite elsewhere",
        "rainfall": "900–1200 mm, northeast monsoon Oct–Dec",
        "temperature": "Hot 28–38°C, no cold season",
        "major_crops": ["Rice", "Sugarcane", "Cotton", "Maize", "Banana", "Groundnut"],
        "disease_pressure": {"bacterial_leaf_blight": "HIGH", "rice_blast": "MEDIUM"},
        "risk_season": "October–January (BLB peak); June–August (blast)",
        "water_table": "Shallow 5–15 m in delta",
        "icar_kvk": "TNAU Coimbatore; KVK Thanjavur"
    },
    "Andhra Pradesh (Coastal Tropical)": {
        "soil": "Coastal alluvial, red loam inland",
        "rainfall": "700–1200 mm",
        "temperature": "Hot tropical 28–40°C",
        "major_crops": ["Rice", "Cotton", "Chili", "Tobacco", "Groundnut", "Maize"],
        "disease_pressure": {"bacterial_leaf_blight": "HIGH", "chili_anthracnose": "HIGH", "cotton_bollworm": "MEDIUM"},
        "risk_season": "June–October (all Kharif diseases)",
        "water_table": "Variable",
        "icar_kvk": "ANGRAU Guntur; KVK Kurnool"
    },
    "West Bengal (New Alluvial)": {
        "soil": "New alluvial, fertile, high humidity",
        "rainfall": "1400–2000 mm",
        "temperature": "Hot humid summer 32–38°C, mild winter 10–24°C",
        "major_crops": ["Rice", "Potato", "Jute", "Tea", "Mustard"],
        "disease_pressure": {"rice_blast": "HIGH", "bacterial_leaf_blight": "HIGH", "potato_late_blight": "HIGH"},
        "risk_season": "July–October (rice diseases); November–January (potato blight)",
        "water_table": "Shallow 3–8 m",
        "icar_kvk": "Bidhan Chandra KVK; KVK Siliguri"
    },
    "Gujarat (Sandy Loam)": {
        "soil": "Sandy loam to loamy sand, low fertility",
        "rainfall": "350–800 mm",
        "temperature": "Hot dry 35–46°C summer, mild winter",
        "major_crops": ["Cotton", "Groundnut", "Wheat", "Bajra", "Castor"],
        "disease_pressure": {"cotton_bollworm": "HIGH", "powdery_mildew_cotton": "MEDIUM"},
        "risk_season": "July–October (Kharif pests)",
        "water_table": "Variable 15–50 m",
        "icar_kvk": "AAU Anand; KVK Rajkot"
    },
    "Madhya Pradesh (Black Cotton)": {
        "soil": "Black cotton (Vertisol) and red mixed",
        "rainfall": "600–1200 mm",
        "temperature": "Summer 40–46°C, Winter 6–20°C",
        "major_crops": ["Wheat", "Soybean", "Cotton", "Chili", "Sugarcane"],
        "disease_pressure": {"stripe_rust": "MEDIUM", "powdery_mildew_wheat": "MEDIUM", "chili_anthracnose": "MEDIUM"},
        "risk_season": "November–February (rust); June–September (soybean diseases)",
        "water_table": "Variable 10–30 m",
        "icar_kvk": "JNKVV Jabalpur; KVK Indore"
    },
    "Rajasthan (Arid Loamy)": {
        "soil": "Sandy loam to sand, very low organic matter",
        "rainfall": "100–500 mm (highly variable)",
        "temperature": "Extreme — summer 44–50°C, winter 2–15°C",
        "major_crops": ["Wheat", "Bajra", "Mustard", "Groundnut", "Guar"],
        "disease_pressure": {"stripe_rust": "MEDIUM", "powdery_mildew_wheat": "LOW"},
        "risk_season": "November–February (Rabi diseases)",
        "water_table": "Deep 30–80 m",
        "icar_kvk": "CAZRI Jodhpur; KVK Jaipur"
    },
    "Odisha (Coastal Humid)": {
        "soil": "Alluvial coastal, laterite inland",
        "rainfall": "1200–1500 mm",
        "temperature": "Hot humid 28–38°C",
        "major_crops": ["Rice", "Maize", "Groundnut", "Sugarcane", "Potato"],
        "disease_pressure": {"rice_blast": "HIGH", "bacterial_leaf_blight": "HIGH"},
        "risk_season": "June–November (rice disease season)",
        "water_table": "Shallow coastal 5–12 m",
        "icar_kvk": "OUAT Bhubaneswar; KVK Cuttack"
    },
}

# ═══════════════════════════════════════════════════════════════
# MANDI / MSP PRICES
# ═══════════════════════════════════════════════════════════════

MANDI_PRICES = [
    {"crop": "Wheat",         "state": "Punjab",      "mandi": "Khanna",     "modal_price": 2250, "msp_2025": 2275, "unit": "Rs/qtl"},
    {"crop": "Rice (Common)", "state": "West Bengal", "mandi": "Kolkata",    "modal_price": 2100, "msp_2025": 2183, "unit": "Rs/qtl"},
    {"crop": "Maize",         "state": "Bihar",       "mandi": "Patna",      "modal_price": 1950, "msp_2025": 2090, "unit": "Rs/qtl"},
    {"crop": "Cotton",        "state": "Gujarat",     "mandi": "Rajkot",     "modal_price": 6200, "msp_2025": 7020, "unit": "Rs/qtl"},
    {"crop": "Tomato",        "state": "Delhi",       "mandi": "Azadpur",    "modal_price": 2140, "msp_2025": None,  "unit": "Rs/qtl"},
    {"crop": "Onion",         "state": "Maharashtra", "mandi": "Lasalgaon",  "modal_price": 1560, "msp_2025": None,  "unit": "Rs/qtl"},
    {"crop": "Potato",        "state": "UP",          "mandi": "Agra",       "modal_price": 1080, "msp_2025": None,  "unit": "Rs/qtl"},
    {"crop": "Soybean",       "state": "MP",          "mandi": "Indore",     "modal_price": 4400, "msp_2025": 4892, "unit": "Rs/qtl"},
    {"crop": "Mustard",       "state": "Rajasthan",   "mandi": "Jaipur",     "modal_price": 5200, "msp_2025": 5950, "unit": "Rs/qtl"},
    {"crop": "Groundnut",     "state": "Gujarat",     "mandi": "Junagadh",   "modal_price": 6100, "msp_2025": 6783, "unit": "Rs/qtl"},
    {"crop": "Sugarcane",     "state": "UP",          "mandi": "Lucknow",    "modal_price": 370,  "msp_2025": 340,  "unit": "Rs/qtl"},
    {"crop": "Chili (Dry)",   "state": "AP",          "mandi": "Guntur",     "modal_price": 15800,"msp_2025": None,  "unit": "Rs/qtl"},
]

# ═══════════════════════════════════════════════════════════════
# GOVERNMENT SCHEMES DATA
# ═══════════════════════════════════════════════════════════════

GOVT_SCHEMES = {
    "pm_kisan": {
        "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
        "benefit": "Rs 6,000 per year in 3 equal instalments of Rs 2,000",
        "eligibility": "All landholding farmer families with cultivable land",
        "exclusions": "Former/current MPs, MLAs, Ministers; income tax payers; institutional landholders",
        "how_to_apply": "Visit PM-KISAN portal pmkisan.gov.in or Common Service Centre (CSC)",
        "documents": ["Aadhaar card", "Land records/Khasra", "Bank account with IFSC"]
    },
    "pmfby": {
        "name": "PMFBY (Pradhan Mantri Fasal Bima Yojana)",
        "benefit": "Crop insurance covering yield losses due to natural disasters, disease, pests",
        "premium": "Kharif 2%, Rabi 1.5%, Annual Horticulture/Commercial 5%",
        "how_to_apply": "Through bank at loan time, or CSC/insurance company before cut-off date",
        "documents": ["Aadhaar", "Land records", "Bank passbook", "Crop sowing certificate"]
    },
    "kisan_credit_card": {
        "name": "Kisan Credit Card (KCC)",
        "benefit": "Short-term crop loan at 4% interest per annum (7% – 3% subvention = 4%)",
        "credit_limit": "Up to Rs 3 lakh at concessional rate; above Rs 3 lakh at commercial rate",
        "how_to_apply": "Apply at any bank or cooperative credit society with land records"
    },
    "soil_health_card": {
        "name": "Soil Health Card Scheme",
        "benefit": "Free soil testing and crop-wise fertilizer recommendation card",
        "how_to_apply": "Contact local Agriculture Department or KVK for soil sample collection"
    }
}

# ═══════════════════════════════════════════════════════════════
# AI AGENT PROMPTS
# ═══════════════════════════════════════════════════════════════

AGENT_PROMPTS = {
    "triage_farmer": """You are KrishiAI, the agricultural triage agent for Indian farmers. Your job is to generate a clear, plain-language farm advisory report.

The report MUST follow this exact structure with these section headers in ALL CAPS followed by colon:

WHAT WE FOUND: [2-3 sentence diagnosis of the crop problem in plain language]

CURRENT WEATHER AND SEASON: [1-2 sentences about regional climate risk for this disease]

WHAT YOU MUST DO TODAY: [3-4 specific immediate actions, numbered, simple language]

SPRAY RECOMMENDATION: [Chemical name, exact dosage, frequency, safety instructions]

NATURAL OPTION: [Biological/organic alternative with dosage]

3 MONTH OUTLOOK: [Month 1, Month 2, Month 3 — what to expect and do each month]

Rules:
- Write for a farmer with primary school education
- Use simple Hindi-English mix terminology only if helpful
- No scientific jargon without plain explanation
- Be specific: exact product names, exact dosages
- Refer to ICAR guidelines and local KVK resources
- Keep each section 2-5 sentences maximum
- Respond ONLY with the report — no preamble""",

    "deep_diagnosis": """You are PathoVision, the pathological diagnosis AI agent for agronomists. You perform clinical-level crop disease analysis.

Generate a detailed pathological assessment covering:
1. Pathogen identification with confidence reasoning
2. Disease cycle and infection mechanism in this agro-climate zone
3. Estimated yield impact if untreated (% loss)
4. Stage-appropriate chemical intervention with PHI compliance
5. Resistance management rotation (chemical group alternation)
6. Long-term IPM strategy aligned with ICAR protocols

Format: Clinical paragraphs, approximately 180 words.
Tone: Technical, precise — written for a certified agronomist.
Use ICAR compound registry names and chemical groups where possible.
Include preharvest interval compliance and FSSAI MRL considerations.""",

    "farmer_advisory": """You are the Farmer Communication Agent. Convert the agronomist diagnosis into a warm, clear plain-language advisory for the farmer.

The advisory must:
- Open with what the problem is, in simple terms
- Explain WHY the disease happened (climate, season, farming practice)
- Give 3 numbered steps the farmer should do THIS WEEK
- Explain the spray with exact name, amount per litre, and number of applications
- Close with one encouraging sentence about crop recovery if treatment is applied

Keep to 120 words. Use simple English. Avoid all technical terms.
If the farmer is from Karnataka, Maharashtra, Punjab, or AP — use a warm regional greeting.""",

    "agronomist_report": """You are the Agronomist Technical Reporting Agent. Generate technical notes for the case file.

Include:
- Pathogen full binomial name and taxonomic class
- Recommended chemical groups with mode-of-action codes (FRAC/IRAC)
- PHI (preharvest interval) and WHP (withholding period)
- Resistance risk rating for the primary fungicide/insecticide
- Economic threshold vs observed infestation level
- Resistance management recommendations
- Reference to relevant ICAR/CABI disease management protocol

Format as structured technical notes, ~120 words. Use agronomic terminology.""",

    "vlm_image": """You are PathoVision VLM, a visual language model specialising in crop disease diagnosis from field photographs.

Analyse the uploaded image and provide:
1. Visible symptom description (lesion morphology, colour, pattern, tissue affected)
2. Most likely pathogen class (fungal/bacterial/viral/insect/abiotic)
3. Disease severity estimate (mild/moderate/severe) and % leaf area affected
4. Recommended laboratory confirmation test if any
5. Confidence level (0-100%) in your visual assessment

Keep response to 80 words maximum. Lead with the most likely diagnosis.
If image quality is poor, state this and give best assessment possible.""",

    "chatbot": """You are KrishiAI, a warm, knowledgeable Indian agricultural expert chatbot. You draw from:
- ICAR crop disease profiles for all major Indian crops
- Agropedia open agricultural encyclopedia
- FAO AGRIS research database
- Government scheme data — PM-KISAN, PMFBY, KCC, MSP prices
- APMC mandi prices across 28 Indian states
- IMD weather and seasonal crop calendars
- IPM practices, SRI rice method, organic farming protocols
- Soil health cards and micronutrient deficiency guides

Rules:
- Respond in the SAME LANGUAGE the user writes in (Hindi or English)
- Be warm, practical, specific — like a trusted village agronomist
- Give actionable advice with specific product names and dosages when relevant
- Reference ICAR, KVK, or government schemes when helpful
- Keep responses to ~140 words
- Use plain text — no markdown, no bullets, no asterisks
- If you don't know something specific, say so and suggest the user contact their local KVK""",

    "pdf_report_farmer": """Generate a plain-language farm advisory section for a PDF report. 
Write 3 clear paragraphs:
1. What the disease is and what caused it
2. What treatment was recommended and how to apply it
3. What the farmer should expect over the next 4 weeks

Use simple English. Max 200 words. No markdown formatting.""",

    "pdf_report_agronomist": """Generate a technical agronomist section for a PDF report.
Write 3 clinical paragraphs:
1. Pathological assessment and disease cycle
2. Prescribed chemical protocol with FRAC group, PHI, and MRL compliance notes
3. Long-term IPM and resistance management recommendations

Use technical agronomic language. ~220 words. Reference ICAR protocols.""",
}

# ═══════════════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ═══════════════════════════════════════════════════════════════

def get_disease_by_symptoms(crop: str, symptoms: str, region: str = "") -> dict:
    """
    Match disease profile from crop type and symptom keywords.
    Returns best matching disease profile dict.
    """
    crop_lower = crop.lower()
    sym_lower = symptoms.lower()

    # Crop → candidate diseases
    CROP_MAP = {
        "tomato": ["early_blight", "late_blight", "bacterial_wilt", "abiotic_stress"],
        "wheat":  ["stripe_rust", "powdery_mildew_wheat", "abiotic_stress"],
        "rice":   ["rice_blast", "bacterial_leaf_blight", "abiotic_stress"],
        "cotton": ["cotton_bollworm", "powdery_mildew_cotton", "abiotic_stress"],
        "potato": ["potato_late_blight", "abiotic_stress"],
        "maize":  ["maize_fall_armyworm", "abiotic_stress"],
        "chili":  ["chili_anthracnose", "abiotic_stress"],
    }

    # Symptom keyword scoring
    SYMPTOM_KEYWORDS = {
        "early_blight":          ["concentric", "ring", "target", "brown spot", "halo", "alternaria"],
        "late_blight":           ["water-soaked", "water soaked", "white mycelium", "greasy", "phytophthora", "rapid"],
        "bacterial_wilt":        ["wilt", "droop", "collapse", "ooze", "vascular", "milky"],
        "stripe_rust":           ["rust", "pustule", "orange", "yellow stripe", "linear", "uredinio"],
        "powdery_mildew_wheat":  ["powder", "mildew", "white coat", "blumeria"],
        "powdery_mildew_cotton": ["powdery", "white coating", "leaf curl", "drop"],
        "rice_blast":            ["blast", "spindle", "grey lesion", "lesion", "magnaporthe", "neck"],
        "bacterial_leaf_blight": ["water-soaked margin", "kresek", "blight", "straw", "xanthomonas"],
        "cotton_bollworm":       ["boll", "bollworm", "frass", "hole", "helicoverpa", "larva"],
        "potato_late_blight":    ["water-soaked", "dark brown", "internal browning", "tuber"],
        "maize_fall_armyworm":   ["window", "whorl", "armyworm", "spodoptera", "frass", "hole"],
        "chili_anthracnose":     ["sunken", "dieback", "fruit lesion", "anthracnose", "colletotrichum"],
        "abiotic_stress":        ["yellow", "chlorosis", "tip burn", "stunted", "purple", "nutrient"],
    }

    candidates = []
    for crop_key, diseases in CROP_MAP.items():
        if crop_key in crop_lower:
            candidates = diseases
            break
    if not candidates:
        candidates = list(DISEASE_PROFILES.keys())

    # Score each candidate
    scores = {}
    for disease_key in candidates:
        if disease_key not in DISEASE_PROFILES:
            continue
        keywords = SYMPTOM_KEYWORDS.get(disease_key, [])
        score = sum(1 for kw in keywords if kw in sym_lower)
        scores[disease_key] = score

    # Pick highest score, fallback to abiotic_stress
    best = max(scores, key=scores.get) if scores else "abiotic_stress"
    if scores.get(best, 0) == 0:
        best = "abiotic_stress"

    return DISEASE_PROFILES[best]


def get_regional_data(region: str) -> dict:
    """Return regional agro-climate profile, partial match supported."""
    for key, data in REGIONAL_PROFILES.items():
        if region.lower() in key.lower() or key.lower() in region.lower():
            return data
    # Fallback — generic India profile
    return {
        "soil": "Variable soil types across India",
        "rainfall": "Varies by region",
        "temperature": "Varies by region",
        "major_crops": ["Rice", "Wheat", "Cotton", "Maize", "Tomato"],
        "disease_pressure": {},
        "risk_season": "Monsoon season June–October general risk",
        "icar_kvk": "Contact nearest KVK"
    }


def build_ai_context(crop: str, region: str, symptoms: str, stage: str = "") -> str:
    """Build a rich context string to include in AI prompts."""
    disease = get_disease_by_symptoms(crop, symptoms, region)
    regional = get_regional_data(region)

    context = f"""
CROP CONTEXT:
- Crop: {crop} | Stage: {stage} | Region: {region}
- Farmer-reported symptoms: {symptoms}

BEST-MATCH DISEASE PROFILE (ICAR reference):
- Disease: {disease['name']}
- Pathogen: {disease['pathogen']} ({disease['class']})
- Severity: {disease['severity']}
- Key symptoms: {', '.join(disease['symptoms'][:3])}
- Favourable conditions: {', '.join(disease['conditions'][:2])}
- Primary chemical Rx: {disease['chemical_rx']['primary']}
- Biological Rx: {disease['bio_rx']['primary']}
- IPM: {'; '.join(disease['ipm'][:3])}

REGIONAL AGRO-CLIMATE:
- Soil: {regional['soil']}
- Rainfall: {regional['rainfall']}
- Temperature: {regional['temperature']}
- Risk season: {regional.get('risk_season', 'N/A')}
- ICAR/KVK: {regional.get('icar_kvk', 'Contact nearest KVK')}
""".strip()

    return context