from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

# This view lets logged-in users create a post or reply.
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set "created_by" to the logged-in user
        serializer.save(created_by=self.request.user)
