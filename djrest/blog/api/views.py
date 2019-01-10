from rest_framework import generics
from .serializers import BlogSerializer
from blog.models import BlogPost

class BlogListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogSerializer
