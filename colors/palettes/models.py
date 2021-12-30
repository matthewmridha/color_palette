from django.db import models
from users.models import User

from django.db.models.constraints import UniqueConstraint
# Create your models here.

class Color(models.Model):
    name = models.CharField(max_length=32, unique=True)
    hex = models.CharField(max_length=16, unique=True)

    def save(self, *args, **kwargs):
        
        # Checks if argument starts with '#', if not, adds '#' at start of string
        # To clean data for correct hex value format
        def convert(value):
            hex = value.strip().upper()
            ls = list(hex)
            if ls[0] == '#':
                return ''.join(ls)
            else:
                ls.insert(0, '#')
                return ''.join(ls)

        self.name = self.name.strip().lower()
        self.hex = convert(self.hex)

        return super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.hex

class Palette(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creator')
    is_public = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    last_edited = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=64, unique=True)
    primary_color1 = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='primary1')
    primary_color2 = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL, related_name='primary2')
    secondary_color1 = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='secondary1')
    secondary_color2 = models.ForeignKey(Color, on_delete=models.PROTECT, related_name='secondary2')
    secondary_color3 = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL, related_name='secondary3')
    secondary_color4 = models.ForeignKey(Color, null=True, blank=True, on_delete=models.SET_NULL, related_name='secondary4')
    saved_by = models.ManyToManyField(User, related_name='saved_by')

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = [
                    'primary_color1',
                    'primary_color2',
                    'secondary_color1',
                    'secondary_color2',
                    'secondary_color3',
                    'secondary_color4'
                ], 
                name='unique_palette')
        ]
    
    def __str__(self):
        return self.name

class Favorites(models.Model):
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    palette = models.ForeignKey(Palette, limit_choices_to={'is_public': True}, related_name='favorites', on_delete=models.CASCADE, null=True)

    
class Favorite_Palettes(models.Model):
    saved_by = models.ForeignKey(User, on_delete=models.CASCADE)
    palette = models.ManyToManyField(Palette, limit_choices_to={'is_public': True}, related_name='favorites_palettes')