from django.urls import path, include
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

router.register(r'palettes', views.PalettePublicView, basename='palettes_public')
router.register(r'colors', views.ColorsView, basename='colors')
router.register(r'colors/create', views.ColorsCreateView, basename='colors')
router.register(r'user/palettes', views.PaletteAuthenticatedView, basename='own_palettes')
router.register(r'user/favorites', views.FavoritesView, basename='favorites')

urlpatterns = format_suffix_patterns([
    path('user/save_palette/<str:name>', views.save_palette),
]) 

urlpatterns += router.urls


