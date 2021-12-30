# Generated by Django 3.2.10 on 2021-12-30 02:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('palettes', '0006_alter_favorites_saved_by'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite_Palettes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('palette', models.ManyToManyField(limit_choices_to={'is_public': True}, related_name='favorites_palettes', to='palettes.Palette')),
                ('saved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
