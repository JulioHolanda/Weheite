from django.contrib import admin

from .models import Forum, Profile

admin.site.register(Profile)
admin.site.register(Forum)
