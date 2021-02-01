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
    febre = models.BooleanField("Febre")
    cansaco = models.BooleanField("Cansaço")
    tosse_seca = models.BooleanField("Tosse seca")
    dor_corporal = models.BooleanField("Dores no corpo")
    congestao_nasal = models.BooleanField("Congestão nasal")
    dor_de_cabeca = models.BooleanField("Dor de cabeça")
    conjuntivite = models.BooleanField("Conjuntivite")
    dor_de_gargante = models.BooleanField("Dor de garganta")
    diarreia = models.BooleanField("Diarréia")
    perdeu_palador_ou_olfato = models.BooleanField("Perda do olfato ou paladar")
    erupcao_cutanea_ou_descoloracao = models.BooleanField("Erupção cutânea ou descoloração da pele")

    #aluno = Aluno()
    data_e_hora = models.DateTimeField(auto_now_add=True)
    autorizacao_presenca = models.BooleanField()