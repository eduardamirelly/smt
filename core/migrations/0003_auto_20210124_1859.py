# Generated by Django 3.1.5 on 2021-01-24 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210124_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='turno',
            field=models.CharField(choices=[('Matutino', 'Matutino'), ('Vespertino', 'Vespertino'), ('Noturno', 'Noturno')], max_length=10),
        ),
    ]
