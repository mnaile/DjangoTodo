from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Todo(models.Model):

    user_id = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    title = models.CharField(max_length=40, null=False, blank=False)
    description = models.CharField(max_length=250, null=False, blank=False)

    def __str__(self):
        return f'{self.title}'
