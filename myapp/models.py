from django.db import models

class Agent(models.Model):
    PROVIDER_CHOICES = [
        ('vapi', 'Vapi'),
        ('retell', 'Retell'),
    ]
    provider = models.CharField(max_length=10, choices=PROVIDER_CHOICES)
    agent_name = models.CharField(max_length=100)
    firstMessage = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.agent_name} ({self.provider})"