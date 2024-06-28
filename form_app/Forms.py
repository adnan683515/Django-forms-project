
from django import forms


class contact(forms.Form):
    
    name = forms.CharField(label='User Name')
    email = forms.EmailField(label='User email')
    file = forms.FileField()
    all_tonar = [('HP','HP101'),('Asus','Asus100'),('Redmi','Redmi111')]
    tonar = forms.ChoiceField(choices=all_tonar,   widget=forms.RadioSelect)
    all_clg = [('212101','GoVT.Mujib Clg'),('202010','Feni Govt. clg'),('202011','Govt. ZiA clg'),('202021','Dhaka clg')]
    CollageName = forms.MultipleChoiceField(choices=all_clg, widget=forms.CheckboxSelectMultiple)
    DataBirth = forms.DateField(label='Date of Birth',widget=forms.DateInput(attrs={'type':'date'}))
 
    
        
    