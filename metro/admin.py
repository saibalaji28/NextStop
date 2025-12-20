from django.contrib import admin
from .models import Station, Line, Connection

admin.site.register(Station)
admin.site.register(Line)
admin.site.register(Connection)