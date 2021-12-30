# Generated by Django 3.2.10 on 2021-12-30 02:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('palettes', '0007_favorite_palettes'),
    ]

    operations = [
        migrations.AddField(
            model_name='palette',
            name='saved_by',
            field=models.ManyToManyField(related_name='saved_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
