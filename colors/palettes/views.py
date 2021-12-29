from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import generics, status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet, ModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .models import Color, Palette, Favorites
from .serializers import ColorSerializer, FavoritesSerializer, PaletteSerializer
from users.models import User
# Create your views here.

# LIST and RETRIEVE of Public Palettes. No Authentication required
class PalettePublicView(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Palette.objects.filter(is_public=True)
    serializer_class = PaletteSerializer
    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'name'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'primary_colors__name', 'secondary_colors__name']

# LIST, CREATE, RETRIEVE, DELETE Palettes for Authenticated users.
# Search By name
class PaletteAuthenticatedView(
    ListModelMixin,
    CreateModelMixin,
    UpdateModelMixin,
    DestroyModelMixin,
    RetrieveModelMixin,
    GenericViewSet
    ):
    permission_class = [IsAuthenticated]
    serializer_class = PaletteSerializer
    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'name'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = [
        'name', 
        'primary_color1__hex', 
        'primary_color2__hex',
        'secondary_color1__hex',
        'secondary_color2__hex',
        'secondary_color3__hex',
        'secondary_color4__hex',
        ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return Palette.objects.filter(created_by=user)

    def get_object(self):
        queryset = self.get_queryset()
        name = self.kwargs['name']
        return get_object_or_404(queryset, name=name)

    def retrieve(self, request, name):
        item = self.get_object()
        serializer = self.get_serializer(item)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = PaletteSerializer(queryset, many=True)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

# List all colors
class ColorsView(
    GenericViewSet, 
    ListModelMixin
    ):
    permission_classes = [AllowAny]
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'name'
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'hex']

# Create Colors -> Admin only
class ColorsCreateView(
    GenericViewSet, 
    CreateModelMixin
    ):
    permission_classes = [IsAdminUser]
    serializer_class = ColorSerializer

# List all Favorites(Paletts) by user, retrieves, updates, deletes
class FavoritesView(ModelViewSet):
    serializer_class = FavoritesSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Favorites.objects.filter(saved_by=user)

    
    












    



    
