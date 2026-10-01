"""Temporary public demo; keep local development settings unchanged."""
from .settings import *
import secrets

DEBUG = False
SECRET_KEY = os.environ.get("DEMO_SECRET_KEY") or secrets.token_urlsafe(48)
ALLOWED_HOSTS = ["localhost", "127.0.0.1", ".trycloudflare.com", ".localhost.run", ".lhr.life"]
ROOT_URLCONF = "app.urls_demo"
DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / ".demo" / "db.sqlite3"}}
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
REST_FRAMEWORK = {"DEFAULT_RENDERER_CLASSES": ["rest_framework.renderers.JSONRenderer"]}
MIDDLEWARE = ["app.demo_middleware.DemoAccessMiddleware", *MIDDLEWARE]
DATA_UPLOAD_MAX_MEMORY_SIZE = 65536
