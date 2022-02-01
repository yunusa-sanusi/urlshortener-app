from django.contrib import admin

from .models import Shortener


class ShorternerAdmin(admin.ModelAdmin):
    list_display = ('long_url', 'short_url', 'count',)


admin.site.register(Shortener, ShorternerAdmin)
