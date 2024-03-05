from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import redirect

from blogpage.models import BlogpostModel, BlogpostContent, Category, Author
from blogpage.serializers import BlogpostSerializer, BlogpostContentSerializer, CategorySerializer, AuthorSerializer


class BlogpostView(viewsets.ModelViewSet):
    queryset = BlogpostModel.objects.all()
    serializer_class = BlogpostSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Redirect to the list view of Blogp ostView using the generated name
        return redirect('blogpostview-list', permanent=False)

    def perform_destroy(self, instance):
        instance.delete()


class BlogpostContentView(viewsets.ModelViewSet):
    queryset = BlogpostContent.objects.all()
    serializer_class = BlogpostContentSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Redirect to the list view of Blogp ostView using the generated name
        return redirect('BlogpostContentView-list', permanent=False)

    def perform_destroy(self, instance):
        instance.delete()


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Redirect to the list view of Blogp ostView using the generated name
        return redirect('Categoryview-list', permanent=False)

    def perform_destroy(self, instance):
        instance.delete()


class AuthorView(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)

        # Redirect to the list view of Blogp ostView using the generated name
        return redirect('AuthorView-list', permanent=False)

    def perform_destroy(self, instance):
        instance.delete()
