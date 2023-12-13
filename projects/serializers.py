from rest_framework.serializers import ModelSerializer

from projects.models import Projects, Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryGetSerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class ProjectsSerializer(ModelSerializer):
    class Meta:
        model = Projects
        fields = "__all__"


class ProjectsListSerializer(ModelSerializer):
    category = CategoryGetSerializer(many=True)

    class Meta:
        model = Projects
        fields = ("id", "title", "thumbnail", "category", "created_at")

    def get_category(self, obj):
        return obj.category
