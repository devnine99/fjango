from config.settings.base import *

DEBUG = True

ALLOWED_HOSTS += ["*"]

# local database
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
CORS_ALLOWED_ORIGINS = [
    "*",
]

# S3
AWS_REGION = "ap-northeast-2"
AWS_STORAGE_BUCKET_NAME = f"{PROJECT_NAME}-prod-bucket"
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.{AWS_REGION}.amazonaws.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=864000"}
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = "public-read"
AWS_S3_SECURE_URLS = True


# REDIS
REDIS_HOST = "localhost"


# CELERY
CELERY_BROKER_URL = f"sqs://"
CELERY_BROKER_TRANSPORT_OPTIONS = {
    "region": "ap-northeast-2",
    "queue_name_prefix": f"{PROJECT_NAME}-dev-",
}


# MEDIA
MEDIA_ROOT = BASE_DIR / "_media"
MEDIA_URL = "/_media/"


# STATIC
STATIC_ROOT = BASE_DIR / "_static"
STATIC_URL = "/_static/"
