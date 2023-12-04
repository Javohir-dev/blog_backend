from rest_framework.serializers import ModelSerializer

from edu.models import EDU


class EDUSerializer(ModelSerializer):
    class Meta:
        model = EDU
        fields = "__all__"


class EDUListSerializer(ModelSerializer):
    class Meta:
        model = EDU
        fields = ("id", "title", "tech", "status", "created_at")
