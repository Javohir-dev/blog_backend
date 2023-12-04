from rest_framework.serializers import ModelSerializer

from info.models import MyInfo, CV


class MyInfoSerializer(ModelSerializer):
    class Meta:
        model = MyInfo
        fields = "__all__"


class CVSerializer(ModelSerializer):
    class Meta:
        model = CV
        fields = "__all__"
