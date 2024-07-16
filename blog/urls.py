from django.contrib import admin
from django.urls import path
from posts.views import posts_view, main_page


urlpatterns = [
    path('admin/', admin.site.urls),
    path('posts/', posts_view),
    path('', main_page),
]
