from django.urls import path, include
from blogpage import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('blogposts', views.BlogpostView, basename='blogpostview')
router.register('blogpostcontent', views.BlogpostContentView,
                basename='blogpostcontentview')
router.register('category', views.CategoryView, basename='categoryview')
router.register('author', views.AuthorView, basename='authorview')

urlpatterns = [
    path('', include(router.urls)),
]
