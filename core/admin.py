from django.contrib import admin
from .models import Aluno, TelefonesDosAlunos, Anamnese

# Register your models here.

admin.site.register(Aluno)
admin.site.register(TelefonesDosAlunos)
admin.site.register(Anamnese)
