# Generated by Django 4.2.2 on 2023-10-01 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='platform',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Android'), (1, 'IoS'), (2, 'Web'), (3, 'Windows'), (4, 'MacOS'), (5, 'Linux')], default=0),
        ),
        migrations.AlterField(
            model_name='device',
            name='registered_on',
            field=models.DateTimeField(auto_created=True, blank=True, null=True),
        ),
    ]
