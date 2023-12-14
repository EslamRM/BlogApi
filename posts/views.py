from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Post
from .serializer import PostSerializer


class PostListView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDeleteView(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
