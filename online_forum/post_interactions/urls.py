from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostCreateView, ThreadPostsListView, like_post, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    # For getting all posts in a thread (custom list endpoint)
    path('threads/<int:thread_id>/posts/', ThreadPostsListView.as_view(), name='thread-posts'),
    # For liking/disliking a post
    path('posts/<int:post_id>/like/', like_post, name='like-post'),
    # For all other CRUD operations on posts (handled by viewset)
    path('', include(router.urls)),
]
