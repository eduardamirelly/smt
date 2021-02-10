from django import forms
from .models import Anamnese

class DataExcelForm(forms.Form):

    file = forms.FileField(widget=forms.TextInput(
        attrs={'type': 'file', 'accept': 'application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})
    )

class ImageStudentForm(forms.Form):
    
    file = forms.FileField(widget=forms.TextInput(
        attrs={'type': 'file', 'accept': 'image/*'})
    )

class MatriculationStudent(forms.Form):
    
    matriculation = forms.CharField(max_length=14, widget=forms.TextInput(
        attrs={'placeholder': 'Digite sua matrícula...'})
    )

class AnamneseForm(forms.ModelForm):
    class Meta:
        model = Anamnese
        fields = ['fever', 'fatigue', 'dry_cough', 'body_ache', 'nasal_congestion', 'headache', 'conjunctivitis', 
        'sore_throat' , 'diarrhea', 'loss_of_taste_or_smell', 'rash_or_discoloration', 'other_symptons']
