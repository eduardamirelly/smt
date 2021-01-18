from django.shortcuts import render
import pandas as pd
from .models import Aluno

# Create your views here.

def listAlunos(request):
    #data = excel_read('core/dataframes/alunos-ifrn-caico.xls')
    #save_data(data)
    
    return render(request, 'listAlunos.html')

def excel_read(filename: str):
    table_alunos = pd.read_excel(filename)
    table_alunos = table_alunos.rename(columns={'Matrícula': 'Matricula', 'Código Curso': 'codeCurso', 'Descrição do Curso': 'descCurso', 'Email Acadêmico': 'emailAcad', 'Situação no Curso': 'statusCurso'})
    
    return table_alunos

def save_data(data):
    list_nomes = []
    list_matriculas = []
    list_campus = []
    list_codeCurso = []
    list_descCurso = []
    list_emailAcad = []
    list_statusCurso = []
    list_telefone = []
    list_turma = []
    list_turno = []
    list_sexo = []

    for x in range(len(data)):
        list_nomes.append(data['Nome'].loc[[x]][x])
        list_matriculas.append(data['Matricula'].loc[[x]][x])
        list_campus.append(data['Campus'].loc[x])
        list_codeCurso.append(data['codeCurso'].loc[x])
        list_descCurso.append(data['descCurso'].loc[x])
        list_emailAcad.append(data['emailAcad'].loc[x])
        list_statusCurso.append(data['statusCurso'].loc[x])
        list_telefone.append(data['Telefone'].loc[x])
        list_turma.append(data['Turma'].loc[x])
        list_turno.append(data['Turno'].loc[x])
        list_sexo.append(data['Sexo'].loc[x])


    aux = []


    for i in range(len(data)):
        nome = list_nomes[i]
        matricula = list_matriculas[i]
        campus = list_campus[i]
        codeCurso = list_codeCurso[i]
        descCurso = list_descCurso[i]
        emailAcad = list_emailAcad[i]
        statusCurso = list_statusCurso[i]
        telefone = list_telefone[i]
        turma = list_turma[i]
        turno = list_turno[i]
        sexo = list_sexo[i]

        obj = Aluno(
            nome = nome,
            matricula = matricula,
            campus = campus,
            code_curso = codeCurso,
            desc_curso = descCurso,
            email_acade = emailAcad,
            sexo = sexo,
            status_curso = statusCurso,
            phone = telefone,
            turma = turma,
            turno = turno,
        )

        aux.append(obj)

    Aluno.objects.bulk_create(aux)




