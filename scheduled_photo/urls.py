from django.conf.urls.defaults import patterns, url
import views

urlpatterns = patterns('',
    url(r'^photo-of-day/add$', views.add, name='scheduled_photo_add'),
    url(r'^photo-of-day/delete/(?P<photo_id>\d+)$', views.delete, name='scheduled_photo_delete'),
    url(r'^photo-of-day/edit/(?P<photo_id>\d+)$', views.edit, name='scheduled_photo_edit'),
)
