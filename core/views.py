from django.shortcuts import render

# Create your views here.

def listAlunos(request):
    return render(request, 'listAlunos.html')
