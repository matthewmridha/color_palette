# Generated by Django 3.2.10 on 2021-12-29 12:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palettes', '0004_alter_favorites_saved_by'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorites',
            name='palette',
        ),
        migrations.AddField(
            model_name='favorites',
            name='palette',
            field=models.ForeignKey(limit_choices_to={'is_public': True}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='favorites', to='palettes.palette'),
        ),
    ]
