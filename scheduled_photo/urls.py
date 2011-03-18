from django.conf.urls.defaults import *


urlpatterns = patterns('scheduled_photo.views',
    url(r'^add$', 'add', name='scheduled_photo_add'),
    url(r'^edit/(?P<photo_id>\d+)$', 'edit', name='scheduled_photo_edit'),
    url(r'^delete/(?P<photo_id>\d+)$', 'delete', name='scheduled_photo_delete'),
)
