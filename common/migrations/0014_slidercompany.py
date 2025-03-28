# Generated by Django 5.1.6 on 2025-03-25 18:42

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0013_slidercontent'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderCompany',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=0.5, size=[1920, 1080], upload_to='SliderCompany/%Y/%m')),
            ],
            options={
                'verbose_name': 'SliderCompany',
                'verbose_name_plural': 'SliderCompany',
                'db_table': 'SliderCompany',
            },
        ),
    ]
