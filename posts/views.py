from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import View
from .models import Post

class PostView(View):
    def get(self, request, post_id=None):
        if post_id:
            # post_detail_view
            post = get_object_or_404(Post, id=post_id)
            return render(request, 'post_detail_view.html', {'post': post})
        else:
            # posts_view
            posts = Post.objects.all()
            return render(request, 'post_list.html', {'posts': posts})
    
    def post(self, request):
        # post_create_view
        return HttpResponse("OK")

class MainPageView(View):
    def get(self, request):
        return render(request, "index.html")
