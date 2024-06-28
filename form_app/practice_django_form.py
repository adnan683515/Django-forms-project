

from django import forms

#widget == filed to html input
class new(forms.Form):
    name = forms.CharField(label="Name:",help_text='Total length must be within 70 characters',required=False,widget=forms.Textarea(attrs={'placeholder':'Enter your name','id':'text_area' ,'class':'class1 class2'}))
    email = forms.EmailField(label="User email",)
    age = forms.IntegerField(label='Your Age',required=False)
    file = forms.FileField()
    weigth = forms.FloatField()
    Balance = forms.DecimalField()
    Birthday = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))
    Appoinment = forms.DateTimeField(widget=forms.DateInput(attrs={'type':'datetime-local'}))
    check = forms.BooleanField()
    CHOICES = [('S','Small'),('M','Medium'),('L','Large')]
    size = forms.ChoiceField(choices=CHOICES,widget=forms.RadioSelect)
    MEAL = [('P','Pepperoni'),('M','Mashroom'),('B','Beef')]
    pizza = forms.MultipleChoiceField(choices=MEAL,widget=forms.CheckboxSelectMultiple)
    
    
    
    
