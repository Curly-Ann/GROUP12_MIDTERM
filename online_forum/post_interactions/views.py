from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer

# Allows logged-in users to create a post or reply.
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        # Automatically set "created_by" to the logged-in user
        serializer.save(created_by=self.request.user)

# Lists all posts under a specific thread by thread_id.
class ThreadPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Post.objects.filter(thread_id=thread_id).order_by('created_at')
