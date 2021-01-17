from django.shortcuts import render
import pandas as pd

# Create your views here.

def listAlunos(request):
    table_alunos = pd.read_excel('core/dataframes/alunos-ifrn-caico.xls')
    table_alunos = table_alunos.rename(columns={'Matrícula': 'Matricula', 'Código Curso': 'codeCurso', 'Descrição do Curso': 'descCurso', 'Email Acadêmico': 'emailAcad', 'Situação no Curso': 'statusCurso'})

    list_header = table_alunos.columns

    return render(request, 'listAlunos.html', {'list_header': list_header})
