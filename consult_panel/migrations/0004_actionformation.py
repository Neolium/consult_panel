# Generated by Django 2.0.5 on 2018-05-12 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consult_panel', '0003_auto_20180511_1622'),
    ]

    operations = [
        migrations.CreateModel(
            name='ActionFormation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
            ],
        ),
    ]
