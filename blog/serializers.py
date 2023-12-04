from rest_framework.serializers import ModelSerializer

from blog.models import Blog


class BlogSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogListSerializer(ModelSerializer):
    class Meta:
        model = Blog
        fields = ("id", "title", "created_at")
