from django.http import HttpResponseRedirect, HttpResponse, HttpResponseServerError, Http404
from django.shortcuts import render_to_response
from django.core.cache import cache

from forms import *
from models import *

def add(request):
    if request.POST and 'photo' in request.POST:
        form = ScheduledPhotoForm(request.POST, request.FILES)
        if form.is_valid:
            new_scheduled_photo = form.save()

    return HttpResponseRedirect(("%s#image%s" % (request.META.get('HTTP_REFERER'), new_scheduled_photo.id)))

    
def delete(request, photo_id):
    try:
        photo = ScheduledPhoto.objects.get(pk=photo_id)
        photo.delete()
        return True
    except:
        return False


def edit(request, photo_id):
    photo = ScheduledPhoto.objects.get(pk=photo_id)
    form = ScheduledPhotoForm(instance=photo)
    return {
        'form':form,
        'photo':photo,
    }

