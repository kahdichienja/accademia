from django import forms
from django.core import validators
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField


User = get_user_model()

class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'full_name',)#'full_name',

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password Miss Match")
        return password2
    def save(self, commit = True):
        user = super(UserAdminCreationForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
class UserAdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'full_name', 'password', 'active', 'admin')#'full_name',
    def clean_password(self):
        return self.initial["password"]


class LoginForm(forms.Form):
    email = forms.CharField(label = 'Email')
    username = forms.CharField(label = 'Usename')
    password = forms.CharField(widget = forms.PasswordInput) 


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            # 'full_name',
            'email',
            'full_name',
            'admission_number',
            'university',
            'username',
            'phone_number',
        )
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email = email)
        if qs.exists():
            raise forms.ValidationError("Email Already Exists")
        return email

    def clean_admission_number(self):
        admission_number = self.cleaned_data.get('admission_number')
        qs = User.objects.filter(admission_number = admission_number)
        if qs.exists():
            raise forms.ValidationError("Admission Number Already Register If It iy You Move To Login Page")
        return admission_number

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        qs = User.objects.filter(phone_number = phone_number)
        if qs.exists():
            raise forms.ValidationError("That Number Already Register")
        return phone_number      

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Password Miss Match")
        return password2
    def save(self, commit = True):
        user = super(RegisterForm,self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        # user.active = False #future update
        if commit:
            user.save()
        return user



# class RegisterForm1(forms.Form):
#     firstname = forms.CharField()
#     surname = forms.CharField() 
#     lastname = forms.CharField() 
#     admnumber = forms.IntegerField(max_length = 13) 
#     phone = forms.IntegerField(max_length = 13) 
#     university = forms.CharField()  
#     email = forms.EmailField()
#     password = forms.CharField(widget = forms.PasswordInput)            
#     password2 = forms.CharField(label = 'Confirm Password', widget = forms.PasswordInput)

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         qs = User.objects.filter(username = username)
#         if qs.exists():
#             raise forms.ValidationError("Username Already Taken")
#         return username                

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         qs = User.objects.filter(email = email)
#         if qs.exists():
#             raise forms.ValidationError("Email Already Exists")
#         return email 
#     def clean(self):
#         data = self.cleaned_data
#         password = self.cleaned_data.get('password')
#         password2 = self.cleaned_data.get('password2')

#         if password != password2:
#             raise forms.ValidationError("Password Miss Match")
#         return data       
