from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet, ReadOnlyModelViewSet

from django_filters.rest_framework import DjangoFilterBackend

from .models import Color, Palette
from .serializers import ColorSerializer, PaletteSerializer
from users.models import User

# Create your views here.

# LIST and RETRIEVE of Palettes. No Authentication required
class PalettePublicView(ReadOnlyModelViewSet):
    permission_classes = [AllowAny]
    queryset = Palette.objects.filter(is_public=True)
    serializer_class = PaletteSerializer
    lookup_field = 'name__iexact'
    lookup_url_kwarg = 'name'
    filter_backends = [filters.SearchFilter]
    search_fields = [
        'name', 
        'primary_color1__hex', 
        'primary_color2__hex',
        'secondary_color1__hex',
        'secondary_color2__hex',
        'secondary_color3__hex',
        'secondary_color4__hex',
    ]

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
    filter_backends = [
        DjangoFilterBackend, 
        filters.SearchFilter
    ]
    search_fields = [
        'name', 
        'primary_color1__hex', 
        'primary_color2__hex',
        'secondary_color1__hex',
        'secondary_color2__hex',
        'secondary_color3__hex',
        'secondary_color4__hex',
        ]
    filterset_fields = [
        'is_public'
    ]

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(created_by=user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        user = self.request.user
        return Palette.objects.filter(created_by=user)
    
    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

# LIST all colors
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

# CREATE Colors -> Admin only
class ColorsCreateView(
    GenericViewSet, 
    CreateModelMixin
    ):
    permission_classes = [IsAdminUser]
    serializer_class = ColorSerializer

# LIST all palettes saved to favorites (palette.saved_by includes current user) by current user
class FavoritesView(ListModelMixin, GenericViewSet):
    serializer_class = PaletteSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Palette.objects.filter(saved_by=user)

# If current user is in palette.saved_by, remove user, else add user
@api_view(['GET'])
def save_palette(request, name):
    if request.method == 'GET':
        palette = get_object_or_404(Palette, name=name, is_public=True)
        user = request.user
        if user in palette.saved_by.all():
            palette.saved_by.remove(user)
        else:
            palette.saved_by.add(user)
        palette.save()
        return Response(status=status.HTTP_200_OK)


        

    
    












    



    
