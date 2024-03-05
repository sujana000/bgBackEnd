from rest_framework import serializers
from .models import BlogpostModel, BlogpostContent, Category, Author


class BlogpostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogpostModel
        fields = '__all__'


class BlogpostContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogpostContent
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class GetBlogpostSerializer(serializers.ModelSerializer):
    blogpost_content = BlogpostContentSerializer()
    category = CategorySerializer()
    author = AuthorSerializer()

    class Meta:
        model = BlogpostModel
        fields = '__all__'

class BlogpostSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title1 = serializers.CharField(max_length=128)
    title2 = serializers.CharField(max_length=128)
    category = CategorySerializer()
    author = AuthorSerializer()
    image = serializers.ImageField()
    content = BlogpostContentSerializer(many=True)