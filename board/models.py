from django.db import models
from members.models import CustomUser
from django.utils import timezone



class Board(models.Model):
    user = models.ForeignKey(CustomUser, null = True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body = models.TextField(default='default') # body 글자수 제한 X

    def __str__(self):
        return self.title
    
# 관리자 권한
# user: hyobi / password: 1234
 
class Comment(models.Model):
    post = models.ForeignKey(Board, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey(CustomUser, null=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField(default='default')

    def __str__(self):
        return self.user.nickname




