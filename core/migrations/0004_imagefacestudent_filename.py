# Generated by Django 3.1.5 on 2021-03-20 00:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20210319_2000'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagefacestudent',
            name='filename',
            field=models.CharField(blank=True, max_length=35, verbose_name='Filename'),
        ),
    ]
