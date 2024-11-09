from django import forms
from .models import Farmer, Query, Harvest, PlantingReport


# Define GENDER_CHOICES outside the class
GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
]

class FarmerForm(forms.ModelForm):
    sex = forms.ChoiceField(choices=GENDER_CHOICES, label='Gender', widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Farmer
        fields = ['name', 'sex', 'age', 'land_size', 'county', 'subcounty', 'parish', 'village']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter your name', 'class': 'form-control'}),
            'sex': forms.Select(choices=GENDER_CHOICES, attrs={'class': 'form-control'}),  # Sex field added in widgets
            'age': forms.NumberInput(attrs={'placeholder': 'Enter your age', 'class': 'form-control'}),
            'land_size': forms.NumberInput(attrs={'placeholder': 'Land size (acres)', 'class': 'form-control'}),
            'county': forms.TextInput(attrs={'placeholder': 'Enter your county', 'class': 'form-control'}),
            'subcounty': forms.TextInput(attrs={'placeholder': 'Enter your subcounty', 'class': 'form-control'}),
            'parish': forms.TextInput(attrs={'placeholder': 'Enter your parish', 'class': 'form-control'}),
            'village': forms.TextInput(attrs={'placeholder': 'Enter your village', 'class': 'form-control'}),

        }

class QueryForm(forms.ModelForm):
    class Meta:
        model = Query
        fields = ['issue']

class HarvestForm(forms.ModelForm):
    class Meta:
        model = Harvest
        fields = ['season', 'land_size', 'potato_kg']

class PlantingReportForm(forms.ModelForm):
    class Meta:
        model = PlantingReport
        fields = ['season', 'land_size', 'potato_kg', 'planting_date']
