

from django import forms
from django.core import validators

# class s_form (forms.Form):
#     name = forms.CharField(label='Your Full Name: ',widget=forms.TextInput)
    
#     email = forms.CharField(label='Email',widget=forms.EmailInput)
    
#     sh= [('D','Day'),('M','Morning')]
#     shift = forms.ChoiceField(choices=sh,label='Choose Your shift')
    
#     # def clean_name (self):
#     #     valname = self.cleaned_data['name']
#     #     print(self.cleaned_data['name'])
#     #     if len(valname) < 10 :
#     #         raise forms.ValidationError("Enter a name with at least 10 characters")

#     #     return valname
    
#     # def clean_email (self):
#     #     valemail = self.cleaned_data['email']
#     #     if '.com' not in valemail:
#     #         raise forms.ValidationError("Your email must contain .com")
#     #     return valemail
    
#     def clean(self):
#         cleaned_data = super().clean()
#         valname = self.cleaned_data['name']
#         valemail = self.cleaned_data['email']
#         if len(valname) <10:
#             raise forms.ValidationError("Enter a name with at least 10 characters")
#         if '.com' not in valemail:
#             raise forms.ValidationError("Your email must contain .com")

def checkvalue (value):
    if len(value) < 10:
        raise forms.ValidationError("Enter a value at least 10 chars")
class s_form (forms.Form):
    name = forms.CharField(widget=forms.TextInput,validators=[validators.MinLengthValidator(10,message='Enter a value at least 10 chars')])
    email = forms.CharField(widget=forms.EmailInput,validators=[validators.EmailValidator(message='You must be give .com')])
    age = forms.IntegerField(widget=forms.NumberInput, validators=[validators.MaxValueValidator(20,message='Your age must be maximum 20'),validators.MinValueValidator(15,message='Your age must be 15')])
    # file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'],message='Your file extension must be pdf')])
    
class password_project (forms.Form):
    name = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        valname = self.cleaned_data['name']
        oldpass = self.cleaned_data['password']
        newpass = self.cleaned_data['confirm_pass']
        if len(valname) < 5: 
    
            raise forms.ValidationError("Your name at least 5 chars")
          
        if oldpass != newpass:
            raise forms.ValidationError("Email does't match")