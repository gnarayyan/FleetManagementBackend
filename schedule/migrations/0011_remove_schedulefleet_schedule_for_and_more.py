# Generated by Django 4.2.2 on 2023-10-01 17:39

from django.db import migrations, models
import utils.file_rename


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0010_schedulefleet'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='schedulefleet',
            name='schedule_for',
        ),
        migrations.AlterField(
            model_name='schedulefleet',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=utils.file_rename.File.rename),
        ),
    ]
