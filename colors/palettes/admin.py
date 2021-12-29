from django.contrib import admin
from .models import Color, Palette, Favorites
# Register your models here.

admin.site.register(Color)
admin.site.register(Palette)
admin.site.register(Favorites)