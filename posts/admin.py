from django.contrib import admin
from posts.models import Post, Comment, Tag

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'rate', 'created_at', 'updated_at']
    search_fields =['title']
    list_display_links= ['title','id']
    list_editable = ['rate']
    list_filter = ['rate']

admin.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Tag)



