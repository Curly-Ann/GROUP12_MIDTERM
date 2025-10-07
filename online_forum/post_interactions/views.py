from rest_framework import generics, permissions, viewsets
from rest_framework.exceptions import PermissionDenied
from .models import Post, PostLike
from .serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

class PostCreateView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ThreadPostsListView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        thread_id = self.kwargs['thread_id']
        return Post.objects.filter(thread_id=thread_id).order_by('created_at')

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def like_post(request, post_id):
    try:
        post = Post.objects.get(pk=post_id)
    except Post.DoesNotExist:
        return Response({'error': 'Post not found.'}, status=status.HTTP_404_NOT_FOUND)
    is_like = request.data.get('is_like', True)
    like_obj, created = PostLike.objects.update_or_create(
        post=post, user=request.user, defaults={'is_like': is_like}
    )
    message = "Liked" if is_like else "Disliked"
    return Response({'status': message}, status=status.HTTP_200_OK)

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.created_by != self.request.user:
            raise PermissionDenied("You do not have permission to edit this post.")
        serializer.save()

    def perform_destroy(self, instance):
        if instance.created_by == self.request.user or getattr(self.request.user, 'role', None) == 'admin':
            instance.delete()
        else:
            raise PermissionDenied("You do not have permission to delete this post.")
