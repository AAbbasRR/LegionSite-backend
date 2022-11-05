from django.urls import path
from .views import *

app_name = 'comments'
urlpatterns = [
    path('api/listcreate/', CreateCommentView.as_view()),
    path('', ListAllCommentsView.as_view(), name="listcomments"),
    path('confirm/<int:pk>/', ConfirmCommentView.as_view(), name="confirmcomment"),
    path('delete/<int:pk>/', CommentDeleteView.as_view(), name="deletecomment"),
]
