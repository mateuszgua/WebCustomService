# Generated by Django 4.0.6 on 2022-07-30 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meas_data', '0003_alter_measdata_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measdata',
            name='profile',
            field=models.CharField(max_length=100, verbose_name='profile'),
        ),
    ]
