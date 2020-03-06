from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    email = models.EmailField()


class Message(models.Model):
    name = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128, unique=True)
    summary = models.CharField(max_length=256)
    message = models.CharField(max_length=256)
    time = models.DateTimeField(auto_now_add=True)
