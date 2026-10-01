from pathlib import Path
from django.conf import settings
from django.http import Http404
from django.urls import include, path, re_path
from django.views.static import serve

DIST = settings.BASE_DIR.parent / "dist-demo"


def frontend(request, resource=""):
    # Only expose compiled assets, never source files or the database.
    candidate = (DIST / resource).resolve()
    if not candidate.is_relative_to(DIST.resolve()) or resource.endswith(".map"):
        raise Http404
    if candidate.is_file():
        return serve(request, resource, document_root=DIST)
    if Path(resource).suffix:
        raise Http404
    return serve(request, "index.html", document_root=DIST)


def unavailable(request):
    raise Http404


urlpatterns = [
    path("api/", include("product.urls")),
    path("api/", include("news.urls")),
    path("api/", include("inquiries.urls")),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^(?:api|admin)(?:/.*)?$", unavailable),
    re_path(r"^(?P<resource>.*)$", frontend),
]
