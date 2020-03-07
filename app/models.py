from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel


# Create your models here.
class User(AbstractUser, BaseModel):
    '''用户信息记录表'''

    class Meta:
        db_table = 'theme_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name



class Spider(BaseModel):
    '''爬取网站文章记录表'''
    STATUS_CHICES = (
        (0, '传统文化'),
        (1, '生态文明'),
        (2, '党建主题')
    )
    status = models.SmallIntegerField(default=False, choices=STATUS_CHICES, verbose_name='文章内容种类')
    title = models.CharField(max_length=100, verbose_name='文章标题')
    time = models.CharField(max_length=50, verbose_name='文章发表时间')
    address = models.ImageField(max_length=50, verbose_name='文章本地地址')
    website = models.URLField(verbose_name='文章对应爬取地址')

    class Meta:
        db_table = 'spider_article'
        verbose_name = '文章'
        verbose_name_plural = verbose_name

class Message(BaseModel):
    '''联系我们记录表'''
    name = models.CharField(max_length=128, unique=True)
    email = models.CharField(max_length=128, unique=True)
    summary = models.CharField(max_length=256)
    message = models.CharField(max_length=256)

    class Meta:
        db_table = 'message'
        verbose_name = '信息'
        verbose_name_plural = verbose_name
