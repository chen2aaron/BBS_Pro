#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
import app01.urls
# 注意注意注意 因为很重要所以要重复3次 要app01.urls才行
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(app01.urls)),
)
