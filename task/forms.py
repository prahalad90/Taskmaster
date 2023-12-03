
from django import forms
from task.models import taskmaster

class taskForm(forms.ModelForm):
    class Meta:
        model = taskmaster
        fields = ['task','enquiryNo', 'timetaken','comments']
        widgets = {
           'task':forms.Select(attrs={'class':'form-control'}),
           'enquiryNo':forms.TextInput(attrs={'class':'form-control'}),
           'timetaken':forms.TextInput(attrs={'class':'form-control','placeholder': 'Minutes',}),
           'comments':forms.TextInput(attrs={'class':'form-control'}),
        }