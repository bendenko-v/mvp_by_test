from rest_framework_mongoengine import generics, viewsets

from core.models.post import Post
from core.serializers import PostSerializer, UserPostsSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserPostsView(generics.ListAPIView):
    serializer_class = UserPostsSerializer

    def get_queryset(self):
        user_id = self.kwargs['id']
        return Post.objects.filter(author=user_id)
