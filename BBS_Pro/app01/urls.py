#coding: utf8
from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'app01.views.index'),
    url(r'^detail/(\d+)/$', 'app01.views.bbs_detail',name='bbs_detail'),
    url(r'^sub_comment/$', 'app01.views.sub_comment'),
    url(r'^bbs_pub/$', 'app01.views.bbs_pub'),
    url(r'^bbs_sub/$', 'app01.views.bbs_sub'),
    url(r'^category/(\d+)/$', 'app01.views.category'),
    # url(r'', include(app01.urls)),
)
