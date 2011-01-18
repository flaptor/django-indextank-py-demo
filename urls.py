from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^guestbook/', include('guestbook.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'django.views.static.serve', {'path': '/home.html',  'document_root': settings.TEMPLATE_DIRS[0]}),
    (r'^polls/', include('polls.urls')),
    (r'^admin/', include(admin.site.urls)),
)
 
