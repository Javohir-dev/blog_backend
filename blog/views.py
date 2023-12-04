from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView

from blog.paginations import DefaultLimitOffSetPagination

from blog.models import Blog
from blog.serializers import BlogListSerializer, BlogSerializer


class BlogModelViewSet(ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return BlogListSerializer
        else:
            return BlogSerializer


class BlogListCreateAPIView(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    pagination_class = DefaultLimitOffSetPagination
