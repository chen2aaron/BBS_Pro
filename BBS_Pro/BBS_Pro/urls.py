#coding:utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views
import app01.urls
# 注意注意注意 因为很重要所以要重复3次 要app01.urls才行
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include(app01.urls)),

    # url(r'^accounts/login/$', 'django.contrib.auth.views.login',{'template_name':'login.html'}),
    # url(r'^login/$', 'views.Login'),
    # url(r'^acc_login/$', 'views.acc_login'),
    # url(r'^logout/$', 'views.logout_view'),
)
