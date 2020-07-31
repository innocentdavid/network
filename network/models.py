from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="author")
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    totalLikes = models.IntegerField(default=0)
    totalDislikes = models.IntegerField(default=0)
    
    def __str__(self):
        return str(self.id)

class Follower(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following")
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="follower")

    def __str__(self):
        return str(self.id)

class Like(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="like")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="like")

    def __str__(self):
        return str(self.id)

class Dislike(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="dislike")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="dislike")

    def __str__(self):
        return str(self.id)