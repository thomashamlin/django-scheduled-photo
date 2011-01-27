django-scheduled-photo

This Django app provides admins with the ability to upload photos, add captions
and optional URL, and schedule their appearance on a site.  It was initially 
developed to provide a "photo of the day" feature and is fairly rudimentary;
it is designed for use by admins and would require moderation/authorization
features if exposed to non-admin users.

The newest photo is shown by default when no photo for today's date is found.


INSTALLING

Install dependencies:
* sorl-thumbnail 
  https://github.com/sorl/sorl-thumbnail or "pip install sorl-thumbnail"
* sorl prerequisites: PIL or pgmagick (preferred)

In settings.py:
a. add 'scheduled_photo' to INSTALLED_APPS
b. define SCHEDULED_PHOTO_UPLOAD_PATH relative to MEDIA_ROOT,
   e.g. "images/daily/"
c. define SCHEDULED_PHOTO_SIZE in sorl format, e.g. "175x130"
d. configure sorl as needed: THUMBNAIL_PREFIX, THUMBNAIL_BASEDIR, 
   THUMBNAIL_SUBDIR, THUMBNAIL_QUALITY, etc.

Create a template 'scheduled_photo.html' that renders the image or thumbnail as
desired.  Check out the sample template provided; they use the templatetag to 
display today's (or the most recent) photo:
   {% load scheduled_photo_tags %}
   {% scheduled_photo %}

Run "./manage.py syncdb"

Upload and schedule photos through the Django admin.
