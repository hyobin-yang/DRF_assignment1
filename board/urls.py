from django.urls import path
from .views import *

app_name = 'board'

urlpatterns = [
    path('', BoardList.as_view()),
    path('<int:pk>/', BoardDetail.as_view()),
    path('<int:pk>/update/', BoardDetail.as_view(), name='board-update'),
    path('<int:pk>/destroy/', BoardDetail.as_view(), name='board-destroy'),
    path('<int:pk>/comments/', CommentList.as_view(), name='board-comments'),
]

