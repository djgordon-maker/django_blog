from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
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

    queryset = Post.objects.all()
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


def detail_view(request, post_id):
    published = Post.objects.exclude(published_date__exact=None)
    try:
        post = published.get(pk=post_id)
    except Post.DoesNotExist:
        raise Http404
    context = {"post": post}
    return render(request, "blogging/detail.html", context)


class BlogDetailView(DetailView):
    queryset = Post.objects.exclude(published_date__exact=None)
    template_name = "blogging/detail.html"


def stub_view(request, *args, **kwargs):
    body = "Stub View\n\n"
    if args:
        body += "Args:\n"
        body += "\n".join(["t%s" % a for a in args])
    if kwargs:
        body += "Kwargs\n"
        body += "\n".join(["\t%s: %s" % i for i in kwargs.items()])
    return HttpResponse(body, content_type="text/plain")
