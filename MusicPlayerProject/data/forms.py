from django.db import models
from django.forms import forms
from django.forms import ModelForm
from .models import Comment
from django import forms


class AddComment(ModelForm):
    class Meta:
        model = Comment
        fields = ['commentz']



class CsvImportForm(forms.Form):
    csv_file = forms.FileField()