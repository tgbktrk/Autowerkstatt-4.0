from django import forms
from cars.models import Car

class CarCreateForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('vin_number', 'licence_plate', 'brand', 'model', 'year', 'color', 'owner', 'picture')
        labels = {
            'vin_number': "Vin Number",
            'licence_plate': "Licence Plate",
            'brand': "Brand",
            'model': "Model",
            'year': "Year",
            'color': "Color",
            'owner': "Owner",
            'picure': "Picture",
        }
        widgets = {
            "vin_number": forms.TextInput(attrs={"class": "form-control",}),
            "licence_plate": forms.TextInput(attrs={"class": "form-control",}),
            "brand": forms.TextInput(attrs={"class": "form-control",}),
            "model": forms.TextInput(attrs={"class": "form-control",}),
            "year": forms.TextInput(attrs={"class": "form-control",}),
            "color": forms.TextInput(attrs={"class": "form-control",}),
            "owner": forms.TextInput(attrs={"class": "form-control",}),
            "picure": forms.ClearableFileInput(attrs={"class": "form-control",}),
        }
        error_messages = {
            "vin_number": {
                "required": "Vin Number is required",
            },
            "picure": {
                "required": "Picture is required",
            }
        }

class CarEditForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('vin_number', 'licence_plate', 'brand', 'model', 'year', 'color', 'owner', 'picture')
        labels = {
            'vin_number': "Vin Number",
            'licence_plate': "Licence Plate",
            'brand': "Brand",
            'model': "Model",
            'year': "Year",
            'color': "Color",
            'owner': "Owner",
            'picure': "Picture",
        }
        widgets = {
            "vin_number": forms.TextInput(attrs={"class": "form-control",}),
            "licence_plate": forms.TextInput(attrs={"class": "form-control",}),
            "brand": forms.TextInput(attrs={"class": "form-control",}),
            "model": forms.TextInput(attrs={"class": "form-control",}),
            "year": forms.TextInput(attrs={"class": "form-control",}),
            "color": forms.TextInput(attrs={"class": "form-control",}),
            "owner": forms.TextInput(attrs={"class": "form-control",}),
            "picure": forms.ClearableFileInput(attrs={"class": "form-control",}),
        }
        error_messages = {
            "vin_number": {
                "required": "Vin Number is required",
            },
            "picure": {
                "required": "Picture is required",
            }
        }

class ImageUploadForm(forms.Form):
    image = forms.ImageField()