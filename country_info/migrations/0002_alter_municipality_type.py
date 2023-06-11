# Generated by Django 4.2.2 on 2023-06-10 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_info', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='municipality',
            name='type',
            field=models.CharField(choices=[('R', 'Rural Municipality (गाउँपालिका)'), ('U', 'Urban Municipality (नगरपालिका)'), ('M', 'Metropolitan City (महानगरपालिका)'), ('S', 'Sub - Metropolitan City (उप-महानगरपालिका)')], default='R', max_length=1),
        ),
    ]