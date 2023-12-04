from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from edu.serializers import EDUListSerializer, EDUSerializer
from edu.models import EDU


class EDUModelViewSet(ModelViewSet):
    queryset = EDU.objects.all()
    serializer_class = EDUSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return EDUListSerializer
        return self.serializer_class
