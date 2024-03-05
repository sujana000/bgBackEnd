from django.contrib import admin

# Register your models here.
from .models import BlogpostModel, BlogpostContent, Category, Author


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogpostModel)
class BlogpostModelAdmin(admin.ModelAdmin):
    pass


@admin.register(BlogpostContent)
class BlogpostContentAdmin(admin.ModelAdmin):
    pass
