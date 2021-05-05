from rest_framework.permissions import AllowAny
from rest_framework import generics
from rest_framework import viewsets
from .serializers import TaskSerializer, UserSerializer, PostSerializer
from .models import Task, Post


# userを作成
class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    # JWTトークンを要求しない設定
    permission_classes = (AllowAny,)


# postのリストを取得
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # JWTトークンを要求しない設定
    permission_classes = (AllowAny,)


# postの詳細を1件取得
class PostRetrieveView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # JWTトークンを要求しない設定
    permission_classes = (AllowAny,)


# taskのリストを取得
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # JWTトークンを要求しない設定
    permission_classes = (AllowAny,)


# taskの詳細を1件取得
class TaskRetrieveView(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # JWTトークンを要求しない設定
    permission_classes = (AllowAny,)


# taskの新規作成、更新、削除（ModelViewSetでCRUDが使える）
class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
