from django.contrib import admin
from eventapp.models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'location', 'date')
    search_fields = ('title', 'description', 'location')


admin.site.register(Event, EventAdmin)
