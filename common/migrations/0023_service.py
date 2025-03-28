# Generated by Django 5.1.6 on 2025-03-28 07:18

import django_resized.forms
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0022_coursecontact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('about', models.TextField()),
                ('image', django_resized.forms.ResizedImageField(crop=['middle', 'center'], force_format=None, keep_meta=True, quality=95, scale=None, size=[456, 474], upload_to='services/%Y/%m')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'db_table': 'Service',
            },
        ),
    ]
