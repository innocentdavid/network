from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Post(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="post_author")
    body = models.TextField(blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.id)

class Follower(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="following_user")
    follower = models.ForeignKey("User", on_delete=models.CASCADE, related_name="follower_user")

    def __str__(self):
        return str(self.id)

class Like(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="like_post")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="like_user")

    def __str__(self):
        return str(self.id)

class Dislike(models.Model):
    post = models.ForeignKey("Post", on_delete=models.CASCADE, related_name="dislike_post")
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name="dislike_user")

    def __str__(self):
        return str(self.id)