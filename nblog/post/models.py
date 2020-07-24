import random
from django.conf import settings

from django.db import models

User = settings.AUTH_USER_MODEL

# Create your models here.


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey("Post", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Post(models.Model):

    # parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    other = models.CharField(blank=True, null=True, max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    # objects = TweetManager()
    # def __str__(self):
    #     return self.content
    
    class Meta:
        ordering = ['-id']
    
    @property
    def is_repost(self):
        return self.parent != None
    
    # def save(self, *args, **kwargs):
    #     super(Post, self).save(*args, **kwargs)

    def serialize(self):
        '''
        Feel free to delete!
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(1, 200)
        }