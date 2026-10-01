from .settings_demo import *
ALLOWED_HOSTS = ["localhost", "127.0.0.1"]
if os.environ.get("RENDER_EXTERNAL_HOSTNAME"):
    ALLOWED_HOSTS.append(os.environ["RENDER_EXTERNAL_HOSTNAME"])
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
