# Generated by Django 3.1.5 on 2021-03-16 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_anamnese_registration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrada',
            old_name='datetime',
            new_name='dtenter',
        ),
    ]