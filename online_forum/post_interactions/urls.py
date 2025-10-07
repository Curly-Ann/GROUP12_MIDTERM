from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostCreateView, ThreadPostsListView, like_post, PostViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet, basename='post')

urlpatterns = [
    path('posts/create/', PostCreateView.as_view(), name='create-post'),
    path('threads/<int:thread_id>/posts/', ThreadPostsListView.as_view(), name='thread-posts'),
    path('posts/<int:post_id>/like/', like_post, name='like-post'),
    path('', include(router.urls)),
]
