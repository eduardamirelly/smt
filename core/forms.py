from django import forms

class DadosExcelForm(forms.Form):

    title = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs={'class': 'file-path validate'})
    )
    file = forms.FileField(widget=forms.TextInput(
        attrs={'type': 'file', 'accept': 'application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})
    )

