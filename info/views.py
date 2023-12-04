from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from info.models import MyInfo, CV
from info.serializers import MyInfoSerializer, CVSerializer


class MyInfoView(APIView):
    def get(self, request):
        queryset = MyInfo.objects.last()
        serializer = MyInfoSerializer(queryset)

        return Response(data=serializer.data)


class MyInfoListCreateView(ListCreateAPIView):
    queryset = MyInfo.objects.all()
    serializer_class = MyInfoSerializer


class CVAPIView(APIView):
    def get(self, request):
        queryset = CV.objects.last()
        serializer = CVSerializer(queryset)

        return Response(data=serializer.data)


class CVListCreateView(ListCreateAPIView):
    queryset = CV.objects.all()
    serializer_class = CVSerializer
