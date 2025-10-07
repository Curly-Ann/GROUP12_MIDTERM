from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.SerializerMethodField()
    dislike_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'thread', 'content', 'created_by', 'created_at', 'like_count', 'dislike_count']

    def get_like_count(self, obj):
        return obj.likes.filter(is_like=True).count()

    def get_dislike_count(self, obj):
        return obj.likes.filter(is_like=False).count()

    def validate_content(self, value):
        if not value.strip():
            raise serializers.ValidationError("Content must not be empty.")
        return value
