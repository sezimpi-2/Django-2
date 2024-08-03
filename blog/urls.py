from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls import path
from posts.views import PostView, MainPageView

urlpatterns = [
    path('', MainPageView.as_view(), name='main_page'),
    path('posts/', PostView.as_view(), name='post_list'),
    path('posts/<int:post_id>/', PostView.as_view(), name='post_detail'),
    path('posts/create/', PostView.as_view(), name='post_create'),
]


# Добавьте пути для статических и медиафайлов, если это необходимо
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
