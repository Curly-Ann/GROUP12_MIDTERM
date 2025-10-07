from django.db import models
from accounts.models import User        # Use your custom User!
from threads.models import Thread       # Import Thread model from threads

class Post(models.Model):
    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Post by {self.created_by} in {self.thread}'