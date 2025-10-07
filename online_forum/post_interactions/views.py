from rest_framework import generics, permissions
from .models import Post, PostLike
from .serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

# Allows logged-in users to create a post or reply
class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

# Lists all posts for a specific thread
class ThreadPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Post.objects.filter(thread_id=thread_id).order_by('created_at')

# Like/dislike endpoint: Accepts { "is_like": true/false }
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
    # Get is_like value (defaults to True/like)
    is_like = request.data.get('is_like', True)
    like_obj, created = PostLike.objects.update_or_create(
        post=post, user=request.user, defaults={'is_like': is_like}
    )
    message = "Liked" if is_like else "Disliked"
    return Response({'status': message}, status=status.HTTP_200_OK)
