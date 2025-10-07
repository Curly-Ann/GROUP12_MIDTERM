from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'thread', 'content', 'created_by', 'created_at']

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content must not be empty.")
        return value
