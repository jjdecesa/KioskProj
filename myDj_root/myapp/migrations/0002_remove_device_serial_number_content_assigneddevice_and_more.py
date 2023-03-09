# Generated by Django 4.1.2 on 2022-12-02 02:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='serial_number',
        ),
        migrations.AddField(
            model_name='content',
            name='assignedDevice',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.device'),
        ),
        migrations.AlterField(
            model_name='content',
            name='active',
            field=models.IntegerField(default=0),
        ),
    ]