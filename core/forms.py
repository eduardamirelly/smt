from django import forms

class DataExcelForm(forms.Form):

    file = forms.FileField(widget=forms.TextInput(
        attrs={'type': 'file', 'accept': 'application/vnd.ms-excel, application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'})
    )

