from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from projects.serializers import ProjectsSerializer, ProjectsListSerializer
from projects.models import Projects


class ProjectsModelViewSet(ModelViewSet):
    queryset = Projects.objects.all()
    serializer_class = ProjectsSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return ProjectsListSerializer
        return self.serializer_class

class PostsByCategory(ListAPIView):
    serializer_class = ProjectsSerializer

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return Projects.objects.filter(category__id=category_id)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()

        # Apply pagination
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)