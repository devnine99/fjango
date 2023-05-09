import datetime
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
ROOT_DIR = Path(__file__).resolve().parent.parent.parent.parent


PROJECT_NAME = "#{PROJECT_NAME}"


SECRET_KEY = "pj%2ze09(g)i^joilp-f8gvs)6ou_m036u3ejs^ky&9nse5k92"

ALLOWED_HOSTS = []

LOCAL_APPS = [
    "app.common.apps.CommonConfig",
    "app.user.apps.UserConfig",
]

THIRD_PARTY_APPS = []

DJANGO_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

INSTALLED_APPS = LOCAL_APPS + THIRD_PARTY_APPS + DJANGO_APPS


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = "ko"

TIME_ZONE = "Asia/Seoul"

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

SITE_NAME = "#{PROJECT_NAME}"
SITE_LOGO = "img/logo.png"  # app/staticfiles/static/img/logo.png 변경
DOMAIN = "domain.com"
FRONTEND_URL = f"https://{DOMAIN}"

# APPEND_SLASH
APPEND_SLASH = False

# AUTH_USER_MODEL
AUTH_USER_MODEL = "user.User"

# SOCIAL REGISTER
SOCIAL_REGISTER = True

# APPLICATION
WSGI_APPLICATION = "config.wsgi.application"
ASGI_APPLICATION = "config.routing.application"


# HOST
DEFAULT_HOST = "api"
ROOT_HOSTCONF = "config.hosts"
ROOT_URLCONF = "config.urls"


# MODEL ID
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


# DATABASE ROUTER
DATABASE_ROUTERS = ["config.db_routers.Router"]


# JWT
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": datetime.timedelta(hours=2),
    "REFRESH_TOKEN_LIFETIME": datetime.timedelta(days=7),
    "ROTATE_REFRESH_TOKENS": True,
}


# ALARMTALK
ALARMTALK_PLUS_ID = "**"
ALARMTALK_ID = "**"
ALARMTALK_CLIENT_ID = "**"
ALARMTALK_CLIENT_SECRET = "**"


# CKEDITOR
CKEDITOR_UPLOAD_PATH = "ckeditor/"
CKEDITOR_CONFIGS = {
    "default": {
        "width": "100%",
    },
}


# CELERY
CELERY_ENABLE_UTC = False
CELERY_TIMEZONE = "Asia/Seoul"
CELERYD_SOFT_TIME_LIMIT = 300
CELERYD_TIME_LIMIT = CELERYD_SOFT_TIME_LIMIT + 60
CELERY_TASK_IGNORE_RESULT = True


# KAKAO
KAKAO_CLIENT_ID = "**"
KAKAO_CLIENT_SECRET = "**"
KAKAO_LOGIN_URL = "https://kauth.kakao.com/oauth/authorize?response_type=code&client_id={kakao_client_id}&redirect_uri={SOCIAL_REDIRECT_URL}&state=kakao"

# NAVER
NAVER_CLIENT_ID = "**"
NAVER_CLIENT_SECRET = "**"
NAVER_LOGIN_URL = "https://nid.naver.com/oauth2.0/authorize?response_type=code&client_id={naver_client_id}&redirect_uri={SOCIAL_REDIRECT_URL}&state=naver"

# FACEBOOK
FACEBOOK_CLIENT_ID = "**"
FACEBOOK_CLIENT_SECRET = "**"
FACEBOOK_LOGIN_URL = "https://www.facebook.com/v9.0/dialog/oauth?response_type=code&client_id={facebook_client_id}&redirect_uri={SOCIAL_REDIRECT_URL}&state=facebook"

# GOOGLE
GOOGLE_CLIENT_ID = "**"
GOOGLE_CLIENT_SECRET = "**"
GOOGLE_LOGIN_URL = "https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?response_type=code&client_id={google_client_id}&redirect_uri={SOCIAL_REDIRECT_URL}&state=google&scope=openid"

# APPLE
APPLE_CLIENT_ID = "**"
APPLE_CLIENT_SECRET = """-----BEGIN PRIVATE KEY-----
**
-----END PRIVATE KEY-----"""
APPLE_KEY_ID = "**"
APPLE_TEAM_ID = "**"
APPLE_LOGIN_URL = "https://appleid.apple.com/auth/authorize?response_type=code&client_id={apple_client_id}&redirect_uri={SOCIAL_REDIRECT_URL}&state=apple"
