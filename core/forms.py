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
        fields = ['fever', 'fatigue', 'dry_cough', 'body_ache', 'nasal_congestion', 'headache', 'shortness_of_breathe', 'conjunctivitis',
        'sore_throat' , 'diarrhea', 'loss_of_taste_or_smell', 'rash_or_discoloration', 'other_symptons', 'student',]

        widgets = {
            'fever': forms.TextInput(attrs={'type': 'checkbox'}),
            'fatigue': forms.TextInput(attrs={'type': 'checkbox'}),
            'dry_cough': forms.TextInput(attrs={'type': 'checkbox'}),
            'body_ache': forms.TextInput(attrs={'type': 'checkbox'}),
            'nasal_congestion': forms.TextInput(attrs={'type': 'checkbox'}),
            'headache': forms.TextInput(attrs={'type': 'checkbox'}),
            'shortness_of_breathe': forms.TextInput(attrs={'type': 'checkbox'}),
            'conjunctivitis': forms.TextInput(attrs={'type': 'checkbox'}),
            'sore_throat': forms.TextInput(attrs={'type': 'checkbox'}),
            'diarrhea': forms.TextInput(attrs={'type': 'checkbox'}),
            'loss_of_taste_or_smell': forms.TextInput(attrs={'type': 'checkbox'}),
            'rash_or_discoloration': forms.TextInput(attrs={'type': 'checkbox'}),
            'other_symptons': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'student': forms.HiddenInput(),


        }
