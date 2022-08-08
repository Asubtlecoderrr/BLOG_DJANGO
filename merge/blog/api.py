from .models import *
from .serializer import *
from rest_framework import viewsets
from rest_framework.response import Response
from datetime import date

class PostListViewSet(viewsets.ModelViewSet):

    queryset = Post.objects.all() 
    serializer_class = PostSerializer
    http_method_names=['get','post','put','patch','delete']

class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    http_method_names=['get','post','put','patch','delete']

class ReplyViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.filter(parent= not None)
    serializer_class = ReplySerializer
    http_method_names=['get']

class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.filter(parent=None)
    serializer_class = CommentSerializer
    http_method_names=['get']

class TagViewSet(viewsets.ModelViewSet):

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    http_method_names=['get','post','put','patch','delete']

class UserViewSet(viewsets.ModelViewSet):

    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    http_method_names=['get','put','patch','delete','post']

    def create(self, request):
        user = request.data
        today = date.today()
        dob = list(map(int,user['dob'].split('-')))
        age = today.year - dob[0] - ((today.month, today.day) < ( dob[1],  dob[2]))
        user['age']=age
        new_user = User.objects.create(image=user['image'],dob = user['dob'],username=user['username'],
            first_name=user['first_name'],last_name=user['last_name'],email=user['email'],age=user['age'])
        new_user.save()
        serializer = UserSerializer(new_user)
        
        return Response(serializer.data)
        
class CommentViewSet(viewsets.ModelViewSet):

    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

