from rest_framework import serializers
from blog.models import BlogPost

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = ('pk', 'title', 'description')
        read_only_fields = ['pk', 'title']
