from django.db import models
from django.db.models import fields
from django.views import generic
from django.shortcuts import render
from .models import  Post
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class PostList(LoginRequiredMixin, generic.ListView):
    login_url = 'login'
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/bloghome.html'
    paginate_by = 4



class PostDetail(LoginRequiredMixin, generic.DetailView):
    login_url = 'login'
    model = Post
    template_name = 'blog/post_detail.html'



class addPost(LoginRequiredMixin, generic.CreateView):
    login_url = 'login'
    model = Post
    template_name = 'blog/blog_add.html'
    fields =  '__all__'



class updatePost(LoginRequiredMixin, generic.UpdateView):
    login_url = 'login'
    model = Post
    template_name = 'blog/blog_update.html'
    fields = [
        'title','image','content','author','status'
    ]

