from django.db import models

# Create your models here.


class Task(models.Model):
    task = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    desc = models.TextField(max_length=200, null=True)
    done = models.BooleanField(default=False)
    objects = None

    def __str__(self):
        return(self.task)
