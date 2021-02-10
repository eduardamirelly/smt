# <<<<<<< HEAD
# from django.shortcuts import render, redirect, get_object_or_404
# from .forms import DataExcelForm, AnamneseForm
# from .models import Student, PhonesStudent, Anamnese
# =======
# from django.shortcuts import render, redirect
# from .forms import DataExcelForm, MatriculationStudent
# from .models import Student, PhonesStudent
# >>>>>>> dev

from django.shortcuts import render, redirect, get_object_or_404
from .forms import DataExcelForm, MatriculationStudent, AnamneseForm
from .models import Student, PhonesStudent, Anamnese

from django.core.files.storage import FileSystemStorage
from .import_file import excel_read, save_data
import pandas as pd

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
                redirect('editor-student')
            else:
                print('não')

    else:
        form = MatriculationStudent()

    return render(request, 'loginMatriculation.html', {'form': form})
    

def editorStudent(request):
    return render(request, 'editorStudent.html')


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
    return render(request, 'formAnamnese.html', {'formulario':form})

def deleteAnamnese(request, pk):
    anamnese = get_object_or_404(Anamnese, pk=pk)
    anamnese.delete()
    return redirect('list-anamneses')
