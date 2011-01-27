from django import forms
from models import ScheduledPhoto


class ScheduledPhotoForm(forms.ModelForm):
    class Meta:
        model = ScheduledPhoto
        
from django.forms.models import modelformset_factory
ScheduledPhotoFormset = modelformset_factory(ScheduledPhoto)
