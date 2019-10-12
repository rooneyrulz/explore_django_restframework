from rest_framework import viewsets, permissions
from posts.models import Post
from .serializers import PostSerializer


class PostViewset(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    permission_classes = [
      permissions.AllowAny
    ]
    serializer_class = PostSerializer
