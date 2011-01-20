from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^$', 'guestbook.views.list' ),
    (r'^(?P<object_id>\d+)/$', 'guestbook.views.detail'),
    (r'^search', 'guestbook.views.search'),
    (r'^submit', 'guestbook.views.submit'),
    (r'^create_entries', 'guestbook.views.create_entries_script'),
)
