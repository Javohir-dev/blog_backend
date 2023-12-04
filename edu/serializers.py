from rest_framework.serializers import ModelSerializer

from edu.models import EDU


class EDUSerializer(ModelSerializer):
    class Meta:
        model = EDU
        fields = "__all__"
