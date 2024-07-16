from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post

def posts_view(request):
    posts = Post.objects.all()  # {QuerySet}
    return render(request=request, template_name='post_list.html', context={'posts': posts})


def main_page(request):
    return render(request, template_name="index.html")

