from django.conf.urls import patterns, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
   url(r'^$', 'yarp.views.landing_page', name='index'),
   url(r'^dashboard/login/$', 'dashboard.views.login_page', name='dashboardlogin'),
   url(r'^dashboard/logout/$', 'django.contrib.auth.views.logout',{'next_page': settings.DASHBOARD_URL}),
   url(r'^dashboard/password/$', 'dashboard.views.recover_password', name='dashboardpass'),
   url(r'^dashboard$', 'dashboard.views.landing_page', name='faq'),
   url(r'^(\w+)/$','yarp.views.blog_page', name='blog'),
   
   (r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT, 'show_indexes':True}
    ),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve', 
    {'document_root': settings.MEDIA_ROOT, 
    'show_indexes':True}
   ),
)
