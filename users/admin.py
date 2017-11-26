from django.contrib import admin

from .models import Contestant


@admin.register(Contestant)
class ContestantAdmin(admin.ModelAdmin):

    list_display = ('name', 'username', 'score', 'logged')
