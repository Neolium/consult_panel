# Generated by Django 2.0.5 on 2018-05-12 15:08

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0007_formation_action_formation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='tva',
            field=models.FloatField(default=19.6, validators=[django.core.validators.MinValueValidator(0.9), django.core.validators.MaxValueValidator(58)]),
        ),
    ]