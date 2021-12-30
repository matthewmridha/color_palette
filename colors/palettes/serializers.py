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
    history = serializers.SerializerMethodField()
    primary_color1 = ColorRelatedField(queryset=Color.objects.all())
    primary_color2 = ColorRelatedField(queryset=Color.objects.all(), allow_null=True, required=False)
    secondary_color1 = ColorRelatedField(queryset=Color.objects.all())
    secondary_color2 = ColorRelatedField(queryset=Color.objects.all())
    secondary_color3 = ColorRelatedField(queryset=Color.objects.all(), allow_null=True, required=False)
    secondary_color4 = ColorRelatedField(queryset=Color.objects.all(), allow_null=True, required=False)
    class Meta:
        model = Palette
        exclude = ['saved_by']
        read_only_fields = ['history']

    def get_history(self, obj):
        h = obj.history.all().values('history_date', 'history_id', 'is_public', 'last_edited', 'name', 'primary_color1', 'primary_color2', 'secondary_color1', 'secondary_color2', 'secondary_color3', 'secondary_color4')[1:]
        return h




