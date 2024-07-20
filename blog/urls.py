from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from posts.views import posts_view, main_page, post_detail_view


urlpatterns = ([
    path('admin/', admin.site.urls),
    path('posts/', posts_view),
    path('', main_page),
   path('posts/<int:post_id>/', post_detail_view)
])

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
