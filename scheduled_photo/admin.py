from django.contrib import admin
from models import *

class ScheduledPhotoAdmin(admin.ModelAdmin):
    list_display = ('photo', 'caption')
    search_fields = ('photo', 'caption',)
    
admin.site.register(ScheduledPhoto, ScheduledPhotoAdmin)

