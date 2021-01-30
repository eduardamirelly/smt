from django.shortcuts import render, redirect
from .forms import DadosExcelForm
from .models import Aluno, TelefonesDosAlunos
from django.core.files.storage import FileSystemStorage
from .import_file import ImportarAlunos
import pandas as pd

# Create your views here.

def listarAlunos(request):
    alunos = Aluno.objects.all()
    telefones = TelefonesDosAlunos.objects.all()

    return render(request, 'listAlunos.html', {'alunos': alunos, 'telefones': telefones})

def importarArquivo(request):
    if request.method == 'POST' and len(request.FILES) != 0:
        form = DadosExcelForm(request.POST, request.FILES)
        
        if form.is_valid():
            arquivo = request.FILES['file']
            fs = FileSystemStorage()
            importAlunos = ImportarAlunos()

            if not fs.exists(arquivo.name):
                fs.save(request.POST['title'], arquivo)
                importAlunos.save_data(importAlunos.excel_read(arquivo.name))
            return redirect('listar-alunos')

    else:
        form = DadosExcelForm()

    return render(request, 'importAlunos.html', {'form': form})

