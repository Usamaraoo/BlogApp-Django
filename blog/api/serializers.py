from rest_framework import serializers
from blog.models import (BlogPost, About)


class BlogPostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BlogPost
        fields = ['url', 'title', 'content', 'type', 'publish_date']


class AboutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = About
        fields = [
            'url',
            'topics',
            'blogs',
        ]
