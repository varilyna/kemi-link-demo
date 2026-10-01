from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "slug", "title", "date", "author")
    list_filter = ("date",)
    search_fields = ("title", "slug", "teaser")
