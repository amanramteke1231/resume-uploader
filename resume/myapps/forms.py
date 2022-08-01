from pyexpat import model
from tkinter import Widget
from attr import field
from django import forms
from .models import Resume

STATE_CHOICE = [('mumbai', 'mumbai'),
         ('pune', 'pune'),
         ('chhattisgarh','chhattisgarh'),
         ('j&k','j&k'),]
GANDER_CHOICE = [('Male','Male'), ('Female','Female')]
class Resumeform(forms.ModelForm):
    gander = forms.ChoiceField(choices=GANDER_CHOICE, widget=forms.RadioSelect)
    job_city = forms.MultipleChoiceField(label='job preffered', choices=STATE_CHOICE, widget=forms.CheckboxSelectMultiple)
    
    class Meta:
        model = Resume
        fields = ['id', 'fullname', 'dob','gander','location','city','pin','state','mobile','email','job_city','profile','myfile']
        labels = {'fullname':'FULL NAME', 'dob':'DATE OF BIRTH', 'gander':'GENDER','location':'LOCALITY', 'city':'CITY', 'pin':'PIN CODE','state': 'STATE', 'mobile':'MOBILE NO', 'email':'EMAIL', 'job_city': 'JOB CITY', 'profile': 'PROFILE', 'myfile': 'RESUME'}
        widgets = {
            'fullname': forms.TextInput(attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','id':'datepicker'}),
            'location': forms.TextInput(attrs={'class':'form-control'}),
            # 'job_city': forms.TextInput(attrs={'class':'form-control'}),
            'pin': forms.NumberInput(attrs={'class':'form-control'}),
            'state': forms.Select(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'mobile': forms.NumberInput(attrs={'class':'form-control'}),
        }