from rest_framework import serializers

from .models import Post

from django import forms


class PostSerializer(serializers.ModelSerializer):
    model = Post
    fields = {
        'title', 'description'
    }