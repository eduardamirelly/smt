from django.contrib import admin
from .models import Aluno, TelefonesAlunos, Anamnese

# Register your models here.

admin.site.register(Aluno)
admin.site.register(TelefonesAlunos)
admin.site.register(Anamnese)