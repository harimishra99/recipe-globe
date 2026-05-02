# 🍛 Swad — India's Recipe Hub

Authentic Indian recipes from all 28 states, in regional languages.  
Built with **Django + PostgreSQL (Supabase) + Cloudinary**, deployable to **Vercel**.

---

## 🗂️ Project Structure

```
recipeglobe/
├── recipeglobe_project/     # Django project config
│   ├── settings.py          # All settings (env-driven)
│   ├── urls.py              # Root URL routing
│   └── wsgi.py
├── recipes/                 # Core app
│   ├── models.py            # RegionalLanguage, Country, State, Cuisine, Recipe …
│   ├── views.py             # All page & AJAX views
│   ├── admin.py             # Rich admin with inline editing
│   ├── urls.py
│   ├── context_processors.py
│   └── management/commands/
│       └── seed_india.py    # Seeds all states, languages, cuisines, sample recipes
├── accounts/                # User profile app
│   ├── models.py            # UserProfile (state + language preferences)
│   ├── views.py
│   ├── forms.py             # Custom signup with first/last name
│   └── admin.py
├── templates/
│   ├── base.html            # Navbar, footer, bottom-nav
│   ├── recipes/
│   │   ├── home.html
│   │   ├── recipe_detail.html
│   │   ├── recipe_list.html
│   │   ├── state_detail.html
│   │   ├── cuisine_detail.html
│   │   ├── category_detail.html
│   │   └── partials/
│   │       ├── recipe_card.html
│   │       └── recipe_card_sm.html
│   ├── account/             # allauth overrides
│   │   ├── login.html
│   │   ├── signup.html
│   │   └── logout.html
│   └── accounts/
│       ├── profile.html
│       ├── edit_profile.html
│       └── saved_recipes.html
├── static/
│   ├── css/main.css         # Complete design system
│   └── js/main.js           # Navbar, tabs, save, rating, lang switcher
├── requirements.txt
├── vercel.json
├── build_files.sh
├── Procfile
└── .env.example
```

---

## ⚡ Quick Start (Local)

```bash
# 1. Clone and enter directory
cd recipeglobe

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy env file and fill in values
cp .env.example .env
# Edit .env with your Supabase + Cloudinary credentials

# 5. Run migrations
python manage.py migrate

# 6. Seed all India data (states, languages, cuisines, sample recipes)
python manage.py seed_india

# 7. Create admin user
python manage.py createsuperuser

# 8. Run development server
python manage.py runserver
```

Open → http://127.0.0.1:8000

Admin panel → http://127.0.0.1:8000/admin

---

## 🔑 Google OAuth Setup

1. Go to [console.cloud.google.com](https://console.cloud.google.com)
2. Create a new project → Enable **Google People API**
3. OAuth consent screen → External → fill app name
4. Credentials → Create OAuth 2.0 Client ID → Web Application
5. Authorised redirect URIs:
   - `http://localhost:8000/accounts/google/login/callback/`
   - `https://yourdomain.vercel.app/accounts/google/login/callback/`
6. Copy **Client ID** and **Client Secret**
7. In Django Admin → Sites → edit `example.com` → set your domain
8. In Django Admin → Social Applications → Add:
   - Provider: Google
   - Client ID: (paste)
   - Secret Key: (paste)
   - Sites: move your site to Chosen

---

## 🗄️ Supabase Setup

1. Create project at [supabase.com](https://supabase.com)
2. Go to Settings → Database → Connection String (URI mode)
3. Copy host, user, password, port into your `.env`
4. Make sure SSL mode is `require`

---

## ☁️ Cloudinary Setup

1. Sign up at [cloudinary.com](https://cloudinary.com)
2. Go to Dashboard → copy Cloud Name, API Key, API Secret
3. Paste into `.env`

---

## 🚀 Deploy to Vercel

```bash
npm i -g vercel
vercel login
vercel --prod
```

Set all `.env` variables in Vercel Dashboard → Project Settings → Environment Variables.

---

## 🛠️ Admin Panel Guide

Log in at `/admin` with your superuser account.

| Section | What you can do |
|---|---|
| **States** | Add/edit all Indian states with language, region, cuisine summary, banner image |
| **Regional Languages** | Add languages with native script names |
| **Recipes** | Add recipes with inline ingredients + steps + translations |
| **Translations** | Add recipe translations per language (shown via language switcher) |
| **Cuisines** | Define cuisine traditions, link to states |
| **Categories** | Time-based, occasion, dietary, festival categories |
| **Users / Profiles** | See users' preferred states and languages |

---

## 🗺️ Data Model (Scalable Design)

```
RegionalLanguage
    ↑
Country (India now, others later)
    ↓
State (28 states + 8 UTs)
    ├── primary_language → RegionalLanguage
    ├── additional_languages → RegionalLanguage (M2M)
    └── region (north/south/east/west/central/northeast/union)

Cuisine (Mughlai, Chettinad, Awadhi…)
    └── states → State (M2M)

Category (time/occasion/meal/diet/festival)

Recipe
    ├── country → Country
    ├── state → State
    ├── cuisine → Cuisine
    ├── categories → Category (M2M)
    ├── diet_type (veg/nonveg/vegan/jain/eggetarian)
    ├── festival_tag
    ├── ingredients → Ingredient
    ├── steps → RecipeStep
    └── translations → RecipeTranslation (per language)

UserProfile
    ├── state → State      (personalises feed)
    └── preferred_language → RegionalLanguage
```

To add a new country in future: add a `Country` record, add `State`-equivalent records (or rename to `Region`), and everything else works automatically.

---

## 📱 Features

- ✅ Mobile-first responsive design + bottom navigation
- ✅ Google OAuth + email signup/login
- ✅ Language switcher per recipe (based on state languages)
- ✅ State explorer with region tabs (North/South/East/West/Central/NE/UT)
- ✅ Personalised feed based on user's state
- ✅ Save/bookmark recipes (AJAX, no page reload)
- ✅ Star ratings
- ✅ Ingredient checklist (persisted in localStorage)
- ✅ WhatsApp + Twitter share
- ✅ Trending, Featured, Quick (5min/30min) recipe sections
- ✅ Festival Special recipes
- ✅ Diet filter (Veg / Non-veg / Vegan / Jain / Eggetarian)
- ✅ Rich admin panel (Jazzmin)
- ✅ Scroll animations
- ✅ Supabase PostgreSQL + Cloudinary images
- ✅ Vercel deployment ready

---

© 2024 Developers Infotech Pvt. Ltd. · developersinfotech.in
