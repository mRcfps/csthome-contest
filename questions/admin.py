from django.contrib import admin

from . import models

admin.site.register(models.Single)
admin.site.register(models.Multiple)
