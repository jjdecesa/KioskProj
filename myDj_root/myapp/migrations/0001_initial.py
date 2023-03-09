# Generated by Django 4.1.3 on 2022-11-30 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=128, null=True, unique=True, verbose_name='filename')),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('date_added', models.DateTimeField(default=datetime.datetime.now, null=True)),
                ('active', models.IntegerField(default=1)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, null=True, unique=True, verbose_name='Device Name')),
                ('description', models.CharField(blank=True, max_length=128, null=True)),
                ('serial_number', models.CharField(blank=True, max_length=32, null=True)),
                ('location', models.CharField(blank=True, max_length=32, null=True)),
            ],
        ),
    ]
