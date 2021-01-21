from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):

    class Meta:
        model = Aluno
        fields = '__all__'


class UploadFileExcelForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()


