from rest_framework.permissions import AllowAny
from rest_framework.generics import (
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from ads.models import Post
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, RegisterUserSerializer


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (IsAuthorOrReadOnly, IsAuthenticated)


class UserCreationView(CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = RegisterUserSerializer
