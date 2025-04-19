import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: Keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: Don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG", "False") == "True"

# AUTH_USER_MODEL = "accounts.UserModel"

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    # Django apps
    "django.contrib.admin",  # Django admin interface
    "django.contrib.auth",  # User authentication
    "django.contrib.contenttypes",  # Content type framework
    "django.contrib.sessions",  # Session management
    "django.contrib.messages",  # Message framework
    "django.contrib.staticfiles",  # Static file management
    # Third-party apps
    "corsheaders",  # Cross-origin resource sharing
    "rest_framework",  # Django REST framework for building APIs
    # Custom apps
    "accounts",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",  # CORS middleware
    "django.middleware.security.SecurityMiddleware",  # Security middleware
    "django.contrib.sessions.middleware.SessionMiddleware",  # Session middleware
    "django.middleware.common.CommonMiddleware",  # Common middleware
    "django.middleware.csrf.CsrfViewMiddleware",  # CSRF protection
    "django.contrib.auth.middleware.AuthenticationMiddleware",  # Authentication middleware
    "django.contrib.messages.middleware.MessageMiddleware",  # Message middleware
    "django.middleware.clickjacking.XFrameOptionsMiddleware",  # Prevent clickjacking
]

# Debug Toolbar (optional)
ENABLE_DEBUG_TOOLBAR = os.getenv("ENABLE_DEBUG_TOOLBAR", "False").lower() == "true"
if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS.append("debug_toolbar")  # Add debug toolbar to apps
    MIDDLEWARE.insert(
        0, "debug_toolbar.middleware.DebugToolbarMiddleware"
    )  # Add debug toolbar to middleware

ROOT_URLCONF = "achare_auth.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "achare_auth.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "achare_authDB.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
