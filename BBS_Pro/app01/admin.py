#coding: utf8
from django.contrib import admin
from app01 import models
# Register your models here.

class BBS_admin(admin.ModelAdmin):
    """
    Description: Model Description
    BBS 列栏 过滤日期 搜索
    """
    list_display = ('title','summary','author','view_count','creat_at',)
    list_filter = ('creat_at',)
    search_fields = ('title','author__user__username',)
admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)
