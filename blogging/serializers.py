from blogging.models import User, Post, Catagory
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ["title", "text", "author"]


class CatagorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Catagory
        fields = ["name", "description", "posts"]
