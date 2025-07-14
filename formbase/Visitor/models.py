from django.db import models

# Create your models here.

class Visitor(models.Model):
    name=models.CharField(max_length=100)
    message=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name