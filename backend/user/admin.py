from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Extra", {"fields": ("full_name", "role")}),
    )
    list_display = ("id", "username", "email", "full_name", "role", "is_staff")
    list_filter = ("role", "is_staff", "is_superuser")

