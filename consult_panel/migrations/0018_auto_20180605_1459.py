# Generated by Django 2.0.5 on 2018-06-05 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0017_auto_20180604_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centreformation',
            name='siret',
            field=models.CharField(blank=True, default='Non renseigné', max_length=14),
        ),
    ]
