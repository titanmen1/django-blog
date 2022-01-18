from django.urls import path

from app.api.views import PostListApiView, PostCRUDApiView, \
    CategoryListApiView, CategoryCRUDApiView, TagListApiView, TagCRUDApiView, \
    CommentListApiView, CommentCRUDApiView

urlpatterns = [
    path('posts/', PostListApiView.as_view(), name='post_list'),
    path('posts/<int:pk>/', PostCRUDApiView.as_view(), name='post_crud'),
    path('categories/', CategoryListApiView.as_view(), name='category_list'),
    path('categories/<int:pk>/', CategoryCRUDApiView.as_view(), name='category_crud'),
    path('tags/', TagListApiView.as_view(), name='tag_list'),
    path('tags/<int:pk>/', TagCRUDApiView.as_view(),
         name='tag_crud'),
    path('comments/', CommentListApiView.as_view(), name='comment_list'),
    path('comments/<int:pk>/', CommentCRUDApiView.as_view(),
         name='comment_crud'),
]
