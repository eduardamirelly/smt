from django.shortcuts import render, redirect
from .forms import DataExcelForm
from .models import Student, PhonesStudent
from django.core.files.storage import FileSystemStorage
from .import_file import excel_read, save_data
import pandas as pd

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

            if not fs.exists(file.name):
                fs.save(file.name, file)
                save_data(excel_read(file.name))

                return redirect('list-students')

    else:
        form = DataExcelForm()

    return render(request, 'importStudents.html', {'form': form})

