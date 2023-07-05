from django.shortcuts import render
from posts.models import Category,Post

def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()

    return render(request,'core/index.html',{
        'posts':posts,
        'categories':category
    })