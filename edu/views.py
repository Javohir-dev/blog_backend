from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from edu.serializers import EDUSerializer
from edu.models import EDU


class EDUModelViewSet(ModelViewSet):
    queryset = EDU.objects.all()
    serializer_class = EDUSerializer
