from django import forms
from .models import AssignmentSubmissionForm



class AssignmentForm(forms.ModelForm):

    full_name = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Full Name', 'hidden': 'true', 'class': 'form-control', 'id': 'full_name', 'required': "true"}))
    admission_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Admission Number', 'hidden': 'true', 'class': 'form-control', 'id': 'admission_number', 'required': "true"}))
    university = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'University', 'hidden': 'true', 'class': 'form-control', 'id': 'university', 'required': "true"}))
    phone_number = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Phone Number', 'hidden': 'true', 'class': 'form-control', 'id': 'phone_number', 'required': "true"}))
    
    class Meta:
        model = AssignmentSubmissionForm
        
        fields = (
            'full_name',
            'admission_number',
            'university',
            'phone_number',
            'file_name',
        )
# class PostForm(forms.Form):