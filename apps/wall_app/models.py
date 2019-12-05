from django.db import models
from ..login_app.models import User

class Message(models.Model):
    message = models.TextField()
    user=models.ForeignKey(User, related_name='messages')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    comment=models.TextField()
    user=models.ForeignKey(User, related_name='user')
    message=models.ForeignKey(Message, related_name='comments')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)