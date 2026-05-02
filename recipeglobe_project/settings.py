from pathlib import Path
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = config('SECRET_KEY', default='django-insecure-change-me-in-production')
DEBUG = config('DEBUG', default=True, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*').split(',')

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'cloudinary_storage',
    'cloudinary',
    'recipes',
    'accounts',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # allauth.account.middleware.AccountMiddleware removed — not compatible with Vercel vendor
]

ROOT_URLCONF = 'recipeglobe_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',
                'recipes.context_processors.site_context',
            ],
        },
    },
]

WSGI_APPLICATION = 'recipeglobe_project.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('DB_NAME', default='postgres'),
        'USER': config('DB_USER', default='postgres'),
        'PASSWORD': config('DB_PASSWORD', default=''),
        'HOST': config('DB_HOST', default='localhost'),
        'PORT': config('DB_PORT', default='5432'),
        'OPTIONS': {'sslmode': config('DB_SSLMODE', default='require')},
        'DISABLE_SERVER_SIDE_CURSORS': True, 
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ('en', 'English'),
    ('hi', 'हिन्दी (Hindi)'),
    ('bn', 'বাংলা (Bengali)'),
    ('te', 'తెలుగు (Telugu)'),
    ('mr', 'मराठी (Marathi)'),
    ('ta', 'தமிழ் (Tamil)'),
    ('gu', 'ગુજરાતી (Gujarati)'),
    ('kn', 'ಕನ್ನಡ (Kannada)'),
    ('ml', 'മലയാളം (Malayalam)'),
    ('pa', 'ਪੰਜਾਬੀ (Punjabi)'),
    ('or', 'ଓଡ଼ିଆ (Odia)'),
    ('as', 'অসমীয়া (Assamese)'),
    ('ur', 'اردو (Urdu)'),
    ('ks', 'कॉशुर (Kashmiri)'),
    ('sa', 'संस्कृत (Sanskrit)'),
    ('ne', 'नेपाली (Nepali)'),
]
LOCALE_PATHS = [BASE_DIR / 'locale']

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=''),
}
MEDIA_URL = '/media/'
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]
SITE_ID = 1

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True
ACCOUNT_FORMS = {'signup': 'accounts.forms.CustomSignupForm'}
SOCIALACCOUNT_LOGIN_ON_GET = True
SOCIALACCOUNT_AUTO_SIGNUP = True

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        },
    }
}

EMAIL_BACKEND = config('EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_HOST = config('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = config('EMAIL_PORT', default=587, cast=int)
EMAIL_USE_TLS = True
EMAIL_HOST_USER = config('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = config('DEFAULT_FROM_EMAIL', default='noreply@swadrecipes.in')

JAZZMIN_SETTINGS = {
    "site_title": "Swad Admin",
    "site_header": "Swad — India's Recipe Hub",
    "site_brand": "🍛 Swad",
    "welcome_sign": "Welcome to Swad Admin Panel",
    "copyright": "Developers Infotech Pvt. Ltd.",
    "search_model": ["recipes.Recipe", "auth.User"],
    "topmenu_links": [
        {"name": "Dashboard", "url": "admin:index"},
        {"name": "Visit Site", "url": "/", "new_window": True},
    ],
    "icons": {
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
        "recipes.Recipe": "fas fa-utensils",
        "recipes.Category": "fas fa-tags",
        "recipes.State": "fas fa-map-marker-alt",
        "recipes.RegionalLanguage": "fas fa-language",
        "recipes.Cuisine": "fas fa-globe-asia",
        "accounts.UserProfile": "fas fa-id-card",
    },
    "related_modal_active": True,
    "changeform_format": "horizontal_tabs",
    "theme": "flatly",
    "dark_mode_theme": "darkly",
    "show_ui_builder": False,
}

JAZZMIN_UI_TWEAKS = {
    "navbar": "navbar-dark",
    "sidebar": "sidebar-dark-orange",
    "brand_colour": "navbar-warning",
    "accent": "accent-warning",
    "theme": "flatly",
}

SESSION_ENGINE = 'django.contrib.sessions.backends.db'
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SAMESITE = 'Lax'