from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all().select_related("author").order_by("-date", "-created_at")
    serializer_class = NewsSerializer

    def perform_create(self, serializer):
        user = self.request.user if self.request.user.is_authenticated else None
        serializer.save(author=user)

