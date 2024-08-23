from django import forms
from django.conf import settings
from measurements.models import Measurement

class MeasurementCreateForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('date', 'csv_file', 'txt_file', 'car',)
        labels = {
            'date': "Date Time",
            'csv_file': "CSV File",
            'txt_file': "Problems",
            'car': "Vin Number of the Car"
        }
        widgets = {
            "date": forms.DateTimeInput(attrs={"class": "form-control", "type":"datetime-local",}),
            "csv_file": forms.ClearableFileInput(attrs={"class": "form-control",}),
            "txt_file": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "car": forms.Select(attrs={"class": "form-control"}),
        }
        error_messages = {
            "csv_file": {
                "required": "csv file is required",
            },
            "car": {
                "required": "car vin number is required",
            }
        }

class MeasurementEditForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('date', 'csv_file', 'txt_file', 'car',)
        labels = {
            'date': "Date Time",
            'csv_file': "CSV File",
            'txt_file': "Problems",
            'car': "Vin Number of the Car"
        }
        widgets = {
            "date": forms.DateTimeInput(attrs={"class": "form-control", "type":"datetime-local",}),
            "csv_file": forms.ClearableFileInput(attrs={"class": "form-control",}),
            "txt_file": forms.ClearableFileInput(attrs={"class": "form-control"}),
            "car": forms.Select(attrs={"class": "form-control"}),
        }
        error_messages = {
            
        }

class FileUploadForm(forms.Form):
    file = forms.FileField()