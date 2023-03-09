# Generated by Django 4.1.2 on 2022-12-02 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_device_serial_number_content_assigneddevice_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
        migrations.AddField(
            model_name='device',
            name='devicename',
            field=models.CharField(max_length=64, null=True, unique=True, verbose_name='devicename'),
        ),
    ]
