from django.contrib import admin
from .models import info_client

#@admin.site.register(info_client)


@admin.register(info_client)
class Info_clientAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'join_date')