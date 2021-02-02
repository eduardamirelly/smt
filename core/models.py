from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField('Nome do Aluno', max_length=100)
    matriculation = models.CharField('Matrícula', max_length=14, unique=True)
    
    CAMPUS_CHOICES = [
        ('CA', 'CA')
    ]
    campus = models.CharField(max_length=2, choices=CAMPUS_CHOICES)

    code_course = models.CharField('Código do Curso', max_length=10)
    desc_course = models.TextField('Descrição do Curso')
    email_acad = models.EmailField('E-mail Acadêmico')

    GENDER_CHOICES = [
        ('F', 'Feminino'),
        ('M', 'Masculino'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    STATUS_COURSE_CHOICES = [
        ('M', 'Matriculado'),
        ('D', 'Desativado'),
    ]
    status_course = models.CharField(max_length=1, choices=STATUS_COURSE_CHOICES)
    class_school = models.CharField('Turma', max_length=20)

    SHIFT_CHOICES = [
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
    ]
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES)

    def __str__(self):
        return self.name


class PhonesStudent(models.Model):
    student = models.ForeignKey(Student, on_delete=models.RESTRICT)
    phone = models.CharField('Telefone', max_length=12)

    def __str__(self):
        return self.phone

class Anamnese(models.Model):
    fever = models.BooleanField("Febre")
    fatigue = models.BooleanField("Cansaço")
    dry_cough = models.BooleanField("Tosse seca")
    body_ache = models.BooleanField("Dores no corpo")
    nasal_congestion = models.BooleanField("Congestão nasal")
    headache = models.BooleanField("Dor de cabeça")
    conjunctivitis = models.BooleanField("Conjuntivite")
    sore_throat = models.BooleanField("Dor de garganta")
    diarrhea = models.BooleanField("Diarréia")
    loss_of_taste_or_smell = models.BooleanField("Perda do olfato ou paladar")
    rash_or_discoloration = models.BooleanField("Erupção cutânea ou descoloração da pele")
    other_symptons = models.TextField("Outros sintomas", default="Nenhum")

    #aluno = Aluno()
    datetime = models.DateTimeField(auto_now_add=True)
    attendance_authorization = models.BooleanField(default=True)