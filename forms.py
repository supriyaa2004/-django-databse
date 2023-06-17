from django import forms
from .models import book

class bookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = ['name', 'email' , 'tittle' , 'publisher' , 'year' , 'status' , 'roll']
