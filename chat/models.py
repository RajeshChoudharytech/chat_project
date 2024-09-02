from django.db import models
from django.utils import timezone
from account.models import User


class Conversation(models.Model):
    participants = models.ManyToManyField(User, related_name='conversations')
    is_group_chat = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return ', '.join([user.username for user in self.participants.all()])


class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='messages')
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.sender.username}: {self.content[:50]}"

    def editable(self):
        return (timezone.now() - self.created_at).total_seconds() < 300  # 5 minutes


class UnreadMessage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    unread = models.BooleanField(default=True)
