from django import forms
from .models import Aluno

class UploadFileExcelForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

