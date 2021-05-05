# 管理画面で登録したModelを見れるようにする

from django.contrib import admin
from .models import Task, Post

admin.site.register(Post)
admin.site.register(Task)
