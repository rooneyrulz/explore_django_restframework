from rest_framework import viewsets, permissions
from posts.models import Post
from .serializers import PostSerializer


class PostViewset(viewsets.ModelViewSet):
    permission_classes = [
      permissions.IsAuthenticated
    ]
    serializer_class = PostSerializer

    def get_queryset(self, *args, **kwargs):
        return self.request.user.post_set.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
