from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import views
#http://blog.sina.com.cn/s/blog_7a9c930d01017fg3.html

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djtest_download.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^download$','views.download_conf_zipfile',name='views.download_conf_zipfile'),
    url(r'^test/', views.test),
    url(r'^test2/t=(?P<type>\w+)/ff=(?P<ff>.{1,500})$', views.send_file), #------- just this
	url('^fileDownload/filename=(?P<filename>.{1,500})/$', 'djtest_download.views.file_download'),#download
)
