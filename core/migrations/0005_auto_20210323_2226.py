# Generated by Django 3.1.5 on 2021-03-24 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_imagefacestudent_filename'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anamnese',
            old_name='datetime',
            new_name='anamnese_datetime',
        ),
    ]
