# Generated by Django 4.1.2 on 2022-12-02 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_remove_content_assigneddevice_content_assigneddevice'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='assignedDevice',
        ),
        migrations.AddField(
            model_name='device',
            name='imagePlaylist',
            field=models.ManyToManyField(to='myapp.content'),
        ),
    ]