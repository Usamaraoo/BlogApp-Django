from rest_framework import viewsets, permissions
from blog.models import *
from .serializers import (BlogPostSerializer, AboutSerializer)
from rest_framework.authentication import SessionAuthentication,BasicAuthentication

class BLogPostView(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    # authentication_classes = [SessionAuthentication,BasicAuthentication]
    # permission_classes = (permissions.IsAuthenticated, permissions.IsAdminUser)

class AboutView(viewsets.ModelViewSet):
    queryset = About.objects.all()
    serializer_class = AboutSerializer
