# Generated by Django 5.1.6 on 2025-03-25 18:47

import django_resized.forms
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_slidercompany_name_alter_slidercompany_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slidercompany',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format='JPEG', keep_meta=True, quality=95, scale=0.5, size=[1920, 1080], upload_to='SliderCompany/%Y/%m'),
        ),
    ]
