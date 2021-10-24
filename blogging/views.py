from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from rest_framework import viewsets
from rest_framework import permissions
from blogging.models import User, Post, Catagory
from blogging.serializers import UserSerializer, PostSerializer, CatagorySerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for User
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class PostViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Post
    """

    queryset = Post.objects.all().order_by("-modified_date")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class CatagoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Catagory
    """

    queryset = Catagory.objects.all()
    serializer_class = CatagorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class BlogListView(ListView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/list.html"


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"
