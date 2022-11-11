from django.urls import path
from .views import (
    #PostListView,
    #PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    PostUserView,
    UserPostListView,
    Postimage
)
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('delete_message/<str:pk>', views.deletemessage, name='delete-message'),
    path('post/mypost/', PostUserView.as_view(), name='mypost'),
    path('post/<str:username>/', UserPostListView.as_view(), name='userpost'),
    path('post_detail/<str:pk>/', views.post_detail, name='post-detail'),
    path('post_create/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),
    path('post_create/new/post_image/<int:pk>', Postimage.as_view(), name='blog-image'),
]
