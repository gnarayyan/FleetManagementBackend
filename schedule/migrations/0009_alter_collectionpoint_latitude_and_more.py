# Generated by Django 4.2.2 on 2023-09-27 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0008_alter_collectionpoint_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectionpoint',
            name='latitude',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='collectionpoint',
            name='longitude',
            field=models.CharField(default='', max_length=256),
        ),
    ]
