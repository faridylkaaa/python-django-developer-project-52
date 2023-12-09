from django.db import models

# Create your models here.
class Label(models.Model):
    name = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.name