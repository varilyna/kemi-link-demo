from django.db import models
from django.conf import settings


class News(models.Model):
    slug = models.SlugField(max_length=200, unique=True)

    date = models.DateField(null=True, blank=True)

    title = models.CharField(max_length=255)
    teaser = models.CharField(max_length=300, blank=True)

    tile_image = models.URLField(blank=True)
    cover_image = models.URLField(blank=True)

    content = models.TextField()

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="news",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self) -> str:
        return self.title
