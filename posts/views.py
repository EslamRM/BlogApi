from django.contrib.auth import get_user_model

# Import necessary modules and classes from Django REST framework
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser

# Import custom permissions, model, and serializer for the Post resource
from .permissions import IsAuthorOrReadOnly
from .models import Post
from .serializer import PostSerializer, UserSerializer


class PostViewset(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewset(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
