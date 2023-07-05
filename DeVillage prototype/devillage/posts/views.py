from django.shortcuts import render,get_object_or_404
from . models import Post

def post(request,pk):
    post = get_object_or_404(Post, pk = pk)
    return render(request,'posts/posts.html',{
        'post':post,
    })