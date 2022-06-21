from django.contrib import admin

from .models import Room,Message,topic

admin.site.register(Room)
admin.site.register(Message)
admin.site.register(topic)
# Register your models here.
