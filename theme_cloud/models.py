from django.db import models


# Create your models here.
class User(models.Model):
#用户表
    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    date_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date_joined']
        verbose_name = '用户'
        verbose_name_plural = '用户'
'''
class Data(models.Model):
#爬虫数据表
    title = models.CharField(max_length=128)
    text = models.CharField()
    date_joined = models.CharField(auto_now_add=True)
    
'''

