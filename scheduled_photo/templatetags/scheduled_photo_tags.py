from datetime import date
from django.conf import settings
from django.template import Library
from scheduled_photo.models import ScheduledPhoto
from scheduled_photo.forms import ScheduledPhotoForm

register = Library()

@register.inclusion_tag('scheduled_photo/view.html')
def scheduled_photo(thumb_size=None, use_cache=True, cache_seconds=3600):
    if not thumb_size:
        try:
            thumb_size = settings.SCHEDULED_PHOTO_SIZE
        except:
            thumb_size = "120x120"
    photo = ScheduledPhoto.for_today(use_cache=use_cache, cache_seconds=cache_seconds)
    return {'scheduled_photo': photo,
            'thumb_size': thumb_size,}


@register.inclusion_tag('scheduled_photo/add.html')
def scheduled_photo_form(photo_id=None):
    if photo_id:
        photo = ScheduledPhoto.objects.get(pk=photo_id)
        form = ScheduledPhotoForm(instance=photo)
    else:
        form = ScheduledPhotoForm()
    return {'form': form,}

