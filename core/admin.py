from django.contrib import admin
from .models import Aluno, TelefonesAlunos

# Register your models here.

admin.site.register(Aluno)
admin.site.register(TelefonesAlunos)

class TelefonesInline(admin.StackedInline):
    model = TelefonesAlunos

class AlunoAdmin(admin.ModelAdmin):
    inlines = [
        TelefonesInline,
    ]
