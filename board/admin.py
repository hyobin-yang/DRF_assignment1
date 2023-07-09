from django.contrib import admin
from .models import Board, Comment  # 모델 등록 - 같은 폴더 내 models모듈에서 Board 임포트

# Register your models here.

admin.site.register(Board) # 모델 등록
admin.site.register(Comment)