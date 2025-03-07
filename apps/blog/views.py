from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import PostListSerializer, PostSerializer

class PostListView(ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostListSerializer

class PostDetailView(ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'