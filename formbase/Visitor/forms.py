from django import forms
from .models import Visitor

class VisitorForm(forms.ModelForm):
    class Meta: #when ever u create new class meta is important
        model=Visitor
        fields=['name','message']