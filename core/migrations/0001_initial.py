# Generated by Django 3.1.5 on 2021-01-17 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aluno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome do Aluno')),
                ('matricula', models.CharField(max_length=14, verbose_name='Matrícula')),
                ('campus', models.CharField(choices=[('CA', 'CA')], default='CA', max_length=2)),
                ('code_curso', models.CharField(max_length=10, verbose_name='Código do Curso')),
                ('desc_curso', models.TextField(verbose_name='Descrição do Curso')),
                ('email_acade', models.EmailField(max_length=254, verbose_name='E-mail Acadêmico')),
                ('sexo', models.CharField(choices=[('Feminino', 'F'), ('Masculino', 'M')], max_length=10)),
                ('status_curso', models.CharField(choices=[('M', 'Matriculado'), ('D', 'Desativado')], default='M', max_length=1)),
                ('phone', models.CharField(max_length=12, verbose_name='Telefone')),
                ('turma', models.CharField(max_length=20, verbose_name='Turma')),
                ('turno', models.CharField(choices=[('M', 'Matutino'), ('V', 'Vespertino'), ('N', 'Noturno')], max_length=1)),
            ],
        ),
    ]
