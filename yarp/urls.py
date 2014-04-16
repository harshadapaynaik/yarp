from django.conf.urls import patterns, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
   
   url(r'^dashboard/login/$', 'dashboard.views.login_page', name='dashboardlogin'),
   url(r'^dashboard/logout/$', 'django.contrib.auth.views.logout',{'next_page': settings.DASHBOARD_URL},name='dashboardlogout'),
   url(r'^dashboard/password/$', 'dashboard.views.recover_password', name='dashboardpass'),
   url(r'^dashboard/posts/$', 'dashboard.views.posts_page', name='dashboardposts'),
   url(r'^dashboard/password/$', 'dashboard.views.recover_password', name='dashboardanalytics'),
   url(r'^dashboard/blog/$', 'dashboard.views.blog_page', name='dashboardblog'),
   url(r'^dashboard$', 'dashboard.views.landing_page', name='dashboard'),
   url(r'^dashboard/(?P<slug>[-\w]+)/(?P<action>[-\w]+)/$', 'dashboard.views.editblog_page', name='editblogpost'),
   url(r'^(?P<slug>[-\w]+)/$', 'yarp.views.blog_page', name='blogpost'),
   
  (r'^static/media/(?P<path>.*)$', 'django.views.static.serve', 
    {'document_root': settings.MEDIA_ROOT, 
    'show_indexes':False}
   ),
   (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT, 'show_indexes':False}
    ),
   url(r'^$', 'yarp.views.landing_page', name='index'),
 
)
