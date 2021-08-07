from django.contrib import admin
from django.urls.conf import include

from .models import Poll, Choice

admin.site.register(Poll)
admin.site.register(Choice)