from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app01.views.index'),
    url(r'^detail/(\d+)/$', 'app01.views.bbs_detail'),
    # url(r'', include(app01.urls)),
)
