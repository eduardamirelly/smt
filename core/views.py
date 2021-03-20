from django.shortcuts import render, redirect, get_object_or_404
from django.core.files.storage import FileSystemStorage, default_storage
from django.core.files.images import ImageFile
from django.http import HttpResponse
from .forms import DataExcelForm, MatriculationStudent, AnamneseForm, ImageStudentForm
from .models import Student, PhonesStudent, Anamnese, ImageFaceStudent
from .import_file import excel_read, save_data
import pandas as pd
import os, base64, datetime, io

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
            obj_student = Student.objects.get(matriculation=student)
            file = request.FILES['file']
            filename, fileextension = os.path.splitext(file.name)

            dt = datetime.datetime.now()
            file.name = f'{obj_student.matriculation}_{dt.strftime("%Y-%m-%d_%Hh%Mm%Ss")}{fileextension}'
            
            obj_student.profile_picture = file
            obj_student.save()
    else:
        form = ImageStudentForm()

    data_student = Student.objects.get(matriculation=student) 
    phones_objs = PhonesStudent.objects.all()
    phones = []

    for p in phones_objs:
        if p.student.pk == data_student.pk:
            phones.append(p.phone)

    img_objs = ImageFaceStudent.objects.all()
    imgs_student = []

    for i in img_objs:
        if i.student.pk == data_student.pk:
            imgs_student.append(i)

    return render(request, 'dataStudent.html', {'data_student': data_student, 'phones': phones, 'imgs_student': imgs_student, 'form': form})


def imageInstant(request, student):
    if request.method == 'POST':
        code_str = request.POST['file']
        code_str = base64.b64decode(code_str)
        
        obj_student = Student.objects.get(matriculation=student)

        dt = datetime.datetime.now()
        filename = f'{obj_student.matriculation}_{dt.strftime("%Y-%m-%d_%Hh%Mm%Ss")}.jpg'

        img_new = ImageFaceStudent()
        img_new.student = obj_student
        img = ImageFile(io.BytesIO(code_str), name=filename)
        img_new.filename = filename
        img_new.image = img
        img_new.save()

        return redirect('data-student', student=obj_student.matriculation)

    return render(request, 'photoStudent.html')


def deleteImageInstant(request, student, pk):
    img = get_object_or_404(ImageFaceStudent, pk=pk)
    
    if default_storage.exists(f'students/{img.filename}'):
        default_storage.delete(f'students/{img.filename}')

    img.delete()
    
    return redirect('data-student', student=student)


def registerAnamneseStudent(request, student):
    form = AnamneseForm()
    if request.method == 'POST':
        form = AnamneseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list-anamneses', student=student)
    else:
        a = Anamnese()
        a.student = Student.objects.get(matriculation=student)
        form = AnamneseForm(instance=a)
        return render(request, 'formAnamnese.html', {'form': form, 'student':a.student})


def listAnamneses(request, student):
    anamneses_student = []
    anamneses = Anamnese.objects.all()

    for a in anamneses:
        if a.student.matriculation == student:
            anamneses_student.append(a)

    obj_student = Student.objects.get(matriculation=student)

    return render(request, 'listAnamnese.html', {'anamneses': anamneses_student, 'student': obj_student})


def showAnamnese(request, student, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    student = get_object_or_404(Student, matriculation=student)
    return render(request, 'showAnamnese.html', {'anamnese': anamnese, 'student': student})


def deleteAnamnese(request, student, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    anamnese.delete()
    return redirect('list-anamneses', student=student)


#função que recebe um json
def enterCampi(request):
    print(request.GET)
    #aqui para gerar o objeto entrada e salvar
    return HttpResponse("Sucesso olá max")
