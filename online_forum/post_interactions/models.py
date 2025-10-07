from django.db import models
from accounts.models import User
from threads.models import Thread

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.created_by} in {self.thread}'

# Model for like/dislike functionality on posts
class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_like = models.BooleanField(default=True)  # True=like, False=dislike

    class Meta:
        unique_together = ('post', 'user')  # Each user can only like/dislike once per post

    def __str__(self):
        status = "Like" if self.is_like else "Dislike"
        return f"{status} by {self.user} on Post {self.post.id}"
