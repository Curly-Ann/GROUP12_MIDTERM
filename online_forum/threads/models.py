from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Thread(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['-created_at']  # Newest threads first
    
    def __str__(self):
        return self.title