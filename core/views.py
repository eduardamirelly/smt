from django.shortcuts import render, redirect, get_object_or_404
from .forms import DataExcelForm, MatriculationStudent, AnamneseForm, ImageStudentForm
from .models import Student, PhonesStudent, Anamnese
from django.core.files.storage import FileSystemStorage
from .import_file import excel_read, save_data
import pandas as pd
import os

# Create your views here.

#Alunos ↓
def listStudents(request):
    students = Student.objects.all()
    phones_students = PhonesStudent.objects.all()

    if len(students) == 0 and len(phones_students) == 0:
        return redirect('upload-file')
    else:
        return render(request, 'listStudents.html', {'students': students, 'phones_students': phones_students})

def importFile(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        form = DataExcelForm(request.FILES)
        
        if form.is_valid():
            file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(file.name, file)
            save_data(excel_read(file.name))

            return redirect('list-students')

    else:
        form = DataExcelForm()

    return render(request, 'importStudents.html', {'form': form})

def loginMatriculationStudent(request):
    if request.method == 'POST':
        form = MatriculationStudent(request.POST)

        if form.is_valid():
            if Student.objects.filter(matriculation=request.POST['matriculation']).exists():
                student = Student.objects.get(matriculation=request.POST['matriculation'])
                return redirect('data-student', pk=student.pk)

    else:
        form = MatriculationStudent()

    return render(request, 'loginMatriculation.html', {'form': form})
    

def dataStudent(request, pk):

    if request.method == 'POST' and len(request.FILES) != 0:
        form = ImageStudentForm(request.FILES)

        if form.is_valid():

            student = Student.objects.get(pk=pk)
            file = request.FILES['file']

            filename, fileextension = os.path.splitext(file.name)

            file.name = f'user_{pk}{fileextension}'
            
            student.photo = file
            student.save()

    else:
        form = ImageStudentForm()

    data_student = Student.objects.get(pk=pk)
    phones_objs = PhonesStudent.objects.all()
    phones = []

    for p in phones_objs:
        if p.student.pk == pk:
            phones.append(p.phone)


    return render(request, 'dataStudent.html', {'data_student': data_student, 'phones': phones, 'form': form})

def imageInstant(request, pk):
    return render(request, 'photoStudent.html')


#Anamnese ↓
def listAnamneses(request):
    anamneses = Anamnese.objects.all()
    return render(request, 'listAnamnese.html', {'anamneses':anamneses})

def showAnamnese(request, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    return render(request, 'showAnamnese.html', {"anamnese":anamnese})

def registerAnamnese(request):
    form = AnamneseForm()
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-anamneses')
    return render(request, 'formAnamnese.html', {'form': form})

def deleteAnamnese(request, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    anamnese.delete()
    return redirect('list-anamneses')
