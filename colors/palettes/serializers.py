from rest_framework import serializers

from .models import Color, Palette

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class ColorRelatedField(serializers.RelatedField):
    def display_value(self, instance):
        return instance

    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return Color.objects.get(hex=data)

class PaletteSerializer(serializers.ModelSerializer):
    primary_color1 = ColorRelatedField(queryset=Color.objects.all())
    primary_color2 = ColorRelatedField(queryset=Color.objects.all())
    secondary_color1 = ColorRelatedField(queryset=Color.objects.all())
    secondary_color2 = ColorRelatedField(queryset=Color.objects.all())
    secondary_color3 = ColorRelatedField(queryset=Color.objects.all())
    secondary_color4 = ColorRelatedField(queryset=Color.objects.all())
    class Meta:
        model = Palette
        exclude = ['saved_by']




