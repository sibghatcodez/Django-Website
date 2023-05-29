from django.db import models

# Create your models here.
class GlobalChat(models.Model):
    user = models.CharField(max_length=3000)
    msg = models.CharField(max_length=3000)
