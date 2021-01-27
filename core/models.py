from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField('Nome do Aluno', max_length=100)
    matricula = models.CharField('Matrícula', max_length=14)
    
    CAMPUS_CHOICES = [
        ('CA', 'CA')
    ]
    campus = models.CharField(max_length=2, choices=CAMPUS_CHOICES)

    cod_curso = models.CharField('Código do Curso', max_length=10)
    desc_curso = models.TextField('Descrição do Curso')
    email_acad = models.EmailField('E-mail Acadêmico')

    SEXO_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)

    MATRICULADO = 'M'
    DESATIVADO = 'D'
    STATUS_CURSO_CHOICES = [
        (MATRICULADO, 'Matriculado'),
        (DESATIVADO, 'Desativado'),
    ]
    status_curso = models.CharField(max_length=1, choices=STATUS_CURSO_CHOICES, default=MATRICULADO)

    turma = models.CharField('Turma', max_length=20)

    TURNO_CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]
    turno = models.CharField(max_length=10, choices=TURNO_CHOICES)

    def __str__(self):
        return self.nome


class TelefonesDosAlunos(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.RESTRICT)
    telefone = models.CharField('Telefone', max_length=12)

    def __str__(self):
        return self.phone
