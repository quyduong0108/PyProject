
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=1 )
    description = models.TextField()
    content = models.TextField()
    image = models.ImageField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='media/music', null = True)
    
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[str(self.id)])

    def __str__(self):
        return self.title
