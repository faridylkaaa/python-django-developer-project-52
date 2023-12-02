from django.db import models
from django.contrib.auth.models import User
from task_manager.statuses.models import Status

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=75)
    description = models.CharField(max_length=500, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    executor = models.ForeignKey(User, blank=True, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='author')
    timestamp = models.DateTimeField(auto_now_add=True)