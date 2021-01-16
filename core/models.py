from django.db import models

# Create your models here.

class Aluno(models.Model):
    name = models.CharField("Nome do Aluno", max_length=100)
    matricula = models.CharField("Matrícula", max_length=14)
    
    CAICO = 'CA'
    CAMPUS_CHOICES = [
        #deixar apenas um por enquanto
        (CAICO, 'CAICO')
    ]
    campus = models.CharField(max_length=2, choices=CAMPUS_CHOICES, default=CAICO)

    code_curso = models.CharField("Código do Curso", max_length=10)
    desc_curso = models.TextField("Descrição do Curso")
    email_acade = models.EmailField("E-mail Acadêmico")

    FEMININO = 'F'
    MASCULINO = 'M'
    SEXO_CHOICES = [
        (FEMININO, 'Feminino'),
        (MASCULINO, 'Masculino'),
    ]
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, default="-")

    MATRICULADO = 'MATRICULADO'
    DESATIVADO = 'DESATIVADO'
    STATUS_CURSO_CHOICES = [
        (MATRICULADO, 'Matriculado'),
        (DESATIVADO, 'Desativado'),
    ]
    status_curso = models.CharField(max_length=20, choices=STATUS_CURSO_CHOICES, default=MATRICULADO)

    phone = models.CharField("Telefone", max_length=12)
    turma = models.CharField("Turma", max_length=20)

    MATUTINO = 'M'
    VESPERTINO = 'V'
    NOTURNO = 'N'
    TURNO_CHOICES = [
        (MATUTINO, 'Matutino'),
        (VESPERTINO, 'Vespertino'),
        (NOTURNO, 'Noturno'),
    ]
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES, default="-")

