# Generated by Django 3.1.5 on 2021-03-19 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210318_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefacestudent',
            name='time_add',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
