# Generated by Django 5.1.6 on 2025-03-28 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0023_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.FileField(upload_to='')),
                ('title', models.CharField(max_length=256)),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'ServiceType',
                'verbose_name_plural': 'ServiceType',
                'db_table': 'ServiceType',
            },
        ),
    ]
