# coding: utf-8
from django.db import models
# from test.test_imageop import MAX_LEN
from django.contrib.auth.models import User

# Create your models here.


class BBS(models.Model):

    """
    Description: Model Description
    帖子具体内容：题目 摘要 内容 作者 浏览量 置顶 创建时间 更新时间
    """
    titile = models.CharField(max_length=64)
    summary = models.CharField(max_length=256, blank=True, null=True)
    content = models.TextField()
    author = models.ForeignKey('BBS_user')
    view_count = models.IntegerField()
    creat_at = models.DateTimeField()
    ranking = models.IntegerField()
    updated_at = models.DateTimeField()

    def __unicode__(self):
        return self.titile


class Category(models.Model):

    """
    Description: Model Description
    板块名称 版主
    """
    name = models.CharField(max_length=32, unique=True)
    administrator = models.ForeignKey('BBS_user')


class BBS_user(models.Model):

    """
    Description: Model Description
    继承Django的user admin
    加用户扩展:
    个性签名 头像
    ForeignKey 是一对多 无法反向查
    OneToOneField 是一对一
    """
    user = models.OneToOneField(User)
    signature = models.CharField(
        max_length=128, default='This gut is too lazy to leave anything here.')
    photo = models.ImageField(
        upload_to="upload_imgs/", default="upload_imgs/user-1.jpg")

    def __unicode__(self):
        return self.user
