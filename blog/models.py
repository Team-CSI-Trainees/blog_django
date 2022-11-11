from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.db import models
from PIL import Image


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_images')
    class Meta:
        ordering=["-date_posted"]
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
class Post_image(models.Model):
    user = models.OneToOneField(Post, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='post_images')

    def __str__(self):
        return str(self.user)
class Message(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE)
    body=models.TextField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.body[0:20]




