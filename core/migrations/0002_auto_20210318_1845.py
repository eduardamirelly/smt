# Generated by Django 3.1.5 on 2021-03-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefacestudent',
            name='image',
            field=models.ImageField(upload_to='students/'),
        ),
    ]
