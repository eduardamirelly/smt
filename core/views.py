from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from .forms import DataExcelForm, MatriculationStudent, AnamneseForm, ImageStudentForm
from .models import Student, PhonesStudent, Anamnese
from .import_file import excel_read, save_data
import pandas as pd
import os, base64

# Create your views here.

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
                return redirect('data-student', student=student.matriculation)
    else:
        form = MatriculationStudent()

    return render(request, 'loginMatriculation.html', {'form': form})


def dataStudent(request, student):
    if request.method == 'POST' and len(request.FILES) != 0:
        form = ImageStudentForm(request.FILES)
        if form.is_valid():
            student = Student.objects.get(matriculation=student)
            file = request.FILES['file']
            filename, fileextension = os.path.splitext(file.name)
            file.name = f'user_{pk}{fileextension}'
            student.photo = file
            student.save()
    else:
        form = ImageStudentForm()

    data_student = Student.objects.get(matriculation=student)
    phones_objs = PhonesStudent.objects.all()
    phones = []

    for p in phones_objs:
        if p.student.pk == data_student.pk:
            phones.append(p.phone)

    return render(request, 'dataStudent.html', {'data_student': data_student, 'phones': phones, 'form': form})


def imageInstant(request, student):
    if request.POST:
        code_str = request.POST['file']
        code_str = base64.b64decode(code_str)
        obj_student = Student.objects.get(matriculation=student)
        filename = f'core/media/students/{obj_student.matriculation}.jpg'
        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, 'wb') as f:
            f.write(code_str)
            
        return redirect('data-student', student=obj_student.matriculation)

    return render(request, 'photoStudent.html')


def enterAnamneses(request):
    if request.method == 'POST':
        form = MatriculationStudent(request.POST)
        if form.is_valid():
            if Student.objects.filter(matriculation=request.POST['matriculation']).exists():
                return redirect('register-anamnese-student', student=request.POST['matriculation'])
    else:
        form = MatriculationStudent()

    return render(request, 'anamnese.html', {'form': form})


def listAnamneses(request):
    anamneses = Anamnese.objects.all()
    return render(request, 'listAnamnese.html', {'anamneses':anamneses})


def showAnamnese(request, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    return render(request, 'showAnamnese.html', {"anamnese":anamnese})


def registerAnamnese(request):
    #form = AnamneseForm()
    #if request.method == 'POST':
    #    form = AnamneseForm(request.POST)
    #    if form.is_valid():
    #        form.save()
    #        return redirect('list-anamneses')
    return redirect('anamnese')#render(request, 'formAnamnese.html', {'form': form})


def registerAnamneseStudent(request, student):
    form = AnamneseForm()
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-anamneses')
    else:
        a = Anamnese()
        a.student = Student.objects.get(matriculation=student)
        form = AnamneseForm(instance=a)
        return render(request, 'formAnamnese.html', {'form': form, 'student':a.student})


def deleteAnamnese(request, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    anamnese.delete()
    return redirect('list-anamneses')


#função que recebe um json
def enterCampi(request):
    print(request.GET)
    #aqui para gerar o objeto entrada e salvar
    return HttpResponse("Sucesso olá max")

