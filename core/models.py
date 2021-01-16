from django.db import models

# Create your models here.

class Aluno(models.Model):
    nome = models.CharField("Nome do Aluno", max_length=100)
    matricula = models.CharField("Matrícula", max_length=14)
    
    CAICO = 'CA'
    CAMPUS_CHOICES = [
        #deixar apenas um por enquanto
        (CAICO, 'CA')
    ]
    campus = models.CharField(max_length=2, choices=CAMPUS_CHOICES, default=CAICO)

    code_curso = models.CharField("Código do Curso", max_length=10)
    desc_curso = models.TextField("Descrição do Curso")
    email_acade = models.EmailField("E-mail Acadêmico")

    FEMININO = 'Feminino'
    MASCULINO = 'Masculino'
    SEXO_CHOICES = [
        (FEMININO, 'F'),
        (MASCULINO, 'M'),
    ]
    sexo = models.CharField(max_length=10, choices=SEXO_CHOICES)

    MATRICULADO = 'M'
    DESATIVADO = 'D'
    STATUS_CURSO_CHOICES = [
        (MATRICULADO, 'Matriculado'),
        (DESATIVADO, 'Desativado'),
    ]
    status_curso = models.CharField(max_length=1, choices=STATUS_CURSO_CHOICES, default=MATRICULADO)

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
    turno = models.CharField(max_length=1, choices=TURNO_CHOICES)

    def __str__(self):
        return self.nome

