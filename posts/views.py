from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def posts_view(request):
    posts = Post.objects.all()  # {QuerySet}
    return render(request=request, template_name = 'post_list.html', context={'posts': posts})

def post_detail_view(request, post_id):
    post = Post.objects.get(id = post_id)
    return render(request, 'post_detail_view.html', {'post': post})

def main_page(request):
    return render(request, "index.html")

