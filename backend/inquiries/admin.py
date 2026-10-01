from django.contrib import admin

from .models import Inquiry


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", "is_answered", "created_at")
    list_filter = ("is_answered", "created_at")
    search_fields = ("name", "email", "question")
    readonly_fields = ("created_at",)
