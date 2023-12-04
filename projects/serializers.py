from rest_framework.serializers import ModelSerializer

from projects.models import Projects, Category


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class ProjectsListSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = ("id", "title", "thumbnail", "category", "created_at")


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
