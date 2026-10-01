from django.http import JsonResponse


class DemoAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(("/admin", "/api/users")):
            return JsonResponse({"detail": "Unavailable in public demo"}, status=404)
        if request.method not in ("GET", "HEAD", "OPTIONS"):
            if not (request.method == "POST" and request.path == "/api/inquiries/"):
                return JsonResponse({"detail": "Demo catalog is read-only"}, status=403)
        return self.get_response(request)
