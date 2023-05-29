from django.db import models

# Create your models here.
class List(models.Model):
    user = models.CharField(max_length=3000)
    todo_list = models.CharField(max_length=3000)
    date = models.DateField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f'{self.user} {self.todo_list} ({self.date})'