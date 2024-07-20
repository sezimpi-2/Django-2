from django.db import models

class Tag (models.Model):
   name = models.CharField(max_length=100)

class Post(models.Model):
    image = models.ImageField(upload_to='posts_images', null=True, blank=True)
    title = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    tag = models.ManyToManyField(Tag, related_name='posts')

    def __str__(self):
     return f"{self.title}-{self.rate}"

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    text = models.CharField(max_length=100)





