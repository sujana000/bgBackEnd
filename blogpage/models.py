from django.db import models
from .serializers import GetBlogpostSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

class Category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class BlogpostModel(models.Model):
    title1 = models.CharField(max_length=128,null=True,blank=True)
    title2 = models.CharField(max_length=128,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE )
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to='blogpost_images/', null=True, blank=True)

    def __str__(self):
        return self.title1


class BlogpostContent(models.Model):
    blogpost = models.ForeignKey(
        BlogpostModel, related_name='content', on_delete=models.CASCADE)
    subtitle = models.CharField(max_length=128,null=True,blank=True)
    description = models.TextField()

    def __str__(self):
        return f"{self.subtitle} - {self.blogpost.title}"

class BlogpostListView(APIView):
    def get(self, request):
        blogposts = BlogpostModel.objects.all()
        serializer = GetBlogpostSerializer(blogposts, many=True)
        return Response(serializer.data)