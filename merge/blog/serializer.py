from django.urls import path, include
from .models import *
from rest_framework import routers, serializers
from django.contrib.auth import get_user_model
from django.core import serializers as sr
import json
from django.contrib.humanize.templatetags import humanize

User = get_user_model()

class CommentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        fields ="__all__"

class ReplySerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ("text",'author','created_on','parent')

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ('id','author','title','text','created_date','category','date','published_date','tag','image')
    
    def get_date(self,obj):
        
        return humanize.naturaltime(obj.published_date)
    


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        
        fields = "__all__"

    


 