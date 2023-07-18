from django.db import models
from django.utils import timezone

class SubscribedUsers(models.Model):
    first_name = models.CharField(max_length=100)  # Add 'first_name' field
    last_name = models.CharField(max_length=100)   # Add 'last_name' field
    email = models.EmailField(unique=True, max_length=100)
    created_date = models.DateTimeField('Date created', default=timezone.now)

    def __str__(self):
        return self.email
