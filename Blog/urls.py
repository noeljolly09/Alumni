from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view(), name='blog_home'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='blog_post_detail'),
    path('add', views.addPost.as_view(),name='blog_add'),
    path('update/<str:slug>/', views.updatePost.as_view(),name='blog_update'),

]
