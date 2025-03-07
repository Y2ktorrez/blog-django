from rest_framework.generics import ListAPIView
from .models import Post, Heading
from .serializers import PostListSerializer, PostSerializer, HeadingSerializer

class PostListView(ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostListSerializer

class PostDetailView(ListAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'

class PostHeadingsView(ListAPIView):
    serializer_class = HeadingSerializer

    def get_queryset(self):
        post_slug = self.kwargs.get('slug')
        return Heading.objects.filter(post__slug=post_slug)