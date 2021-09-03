from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
STATUS = (
    (False,"Draft"),
    (True,"Publish")
)

class Blog(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE , null=True, blank=True)
    title = models.CharField(max_length=150)
    dsc = models.TextField()
    date = models.DateTimeField(auto_now_add= True, null=True)
    checkbox = models.BooleanField(choices=STATUS, default=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' % (self.post.title, self.name)

# class EditComment(models.Model):
#     body = models.CharField(max_length=50)