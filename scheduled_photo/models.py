from datetime import date
from django.conf import settings
from django.core.cache import cache
from django.db import models
from django.db.models.signals import post_save, post_delete, post_init

class ScheduledPhoto(models.Model):
    """
    Show uploaded photos at specified dates, and manage uploading.
    """
    start_date = models.DateField()
    photo = models.ImageField(upload_to=settings.SCHEDULED_PHOTO_UPLOAD_PATH, blank=True)
    caption = models.CharField(blank=True, max_length=250)
    target_url = models.CharField(blank=True, max_length=250)
    create_dt = models.DateTimeField(auto_now_add=True)
    update_dt = models.DateTimeField(auto_now=True)
    
    @classmethod
    def for_today(cls, use_cache=True, cache_seconds=3600):
        today = date.today()
        if use_cache:
            key = cache_key(today)
            photo = cache.get(key)
            if photo is None:
                photo = ScheduledPhoto.for_date(today)
                cache.set(key, photo, cache_seconds)
        else:
            photo = ScheduledPhoto.for_date(today)

        return photo

    @classmethod
    def for_date(cls, the_date):
        try:
            return ScheduledPhoto.objects.filter(start_date__lte=the_date).order_by('-start_date')[0]
        except IndexError:
            return None

    def __unicode__(self):
        return "%s: %s" % (self.photo, self.caption)

    class Meta:
        verbose_name_plural = 'Photo of the day'

def cache_key(the_date=None):
    if not the_date:
        the_date = date.today()
    return 'photo_%s' % the_date.strftime('%Y%m%d')

def _clear_cache(sender, **kwargs):
    photo = kwargs.get('instance')
    key = cache_key()
    # set cache before delete to avoid potential race condition
    cache.set(key, None)
    cache.delete(key)

post_save.connect(_clear_cache, sender=ScheduledPhoto, weak=False)
post_delete.connect(_clear_cache, sender=ScheduledPhoto, weak=False)

