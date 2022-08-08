from blog import api
from django.urls import path, include
from rest_framework import routers
from blog.api import *
router  =routers.DefaultRouter()
router.register(r'blog',api.PostListViewSet)
router.register(r'category',api.CategoryViewSet)
router.register(r'tag',api.TagViewSet)
router.register(r'user',api.UserViewSet)
router.register(r'comment',api.CommentViewSet)
router.register(r'reply',api.ReplyViewSet)
urlpatterns = [
    
    path('',include(router.urls)),
]
