# Generated by Django 3.1.5 on 2021-03-16 18:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_anamnese_student'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anamnese',
            name='registration',
        ),
    ]