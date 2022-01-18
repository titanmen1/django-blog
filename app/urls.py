from django.contrib import admin
from django.urls import path, include

from app.views import PostListView, UserPostListView, PostDetailView, \
    PostCreateView, PostUpdateView, PostDeleteView, add_comment

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('user/<str:username>/', UserPostListView.as_view(),
         name='user_posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post_create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(),
         name='post_update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(),
         name='post_delete'),
    path('post/<int:pk>/comment/', add_comment, name='add_comment'),
]
