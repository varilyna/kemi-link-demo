from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import News

User = get_user_model()


class NewsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        source="author",
        queryset=User.objects.all(),
        write_only=True,
        required=False,
        allow_null=True,
    )

    class Meta:
        model = News
        fields = [
            "id",
            "slug",
            "date",
            "title",
            "teaser",
            "tile_image",
            "cover_image",
            "content",
            "author",
            "author_id",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]
