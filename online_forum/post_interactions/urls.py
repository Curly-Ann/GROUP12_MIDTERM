from django.urls import path
from .views import PostCreateView, ThreadPostsListView, like_post

urlpatterns = [
    # Create a post
    path('posts/create/', PostCreateView.as_view(), name='create-post'),
    # List posts in a thread
    path('threads/<int:thread_id>/posts/', ThreadPostsListView.as_view(), name='thread-posts'),
    # Like/dislike a post
    path('posts/<int:post_id>/like/', like_post, name='like-post'),
]
