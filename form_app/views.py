from django.shortcuts import render
from . Forms import contact
from . practice_django_form import new
from . students_form import s_form,password_project

# Create your views here.
def about(request):
    if request.method == 'POST':
        print(request.POST)
        name = request.POST.get('username')
        email = request.POST.get('email')
        val = request.POST.get('select')
        return render(request,'about.html',{'name':name,'email':email,'val':val})
    else:
        return render(request,'about.html')

def form(request):
   
    return render(request,'form.html')

def Django_Froms(request):
    if request.method == 'POST':
        form = contact(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open ('./form_app/uploadfile/'+file.name ,'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
                        
            print(form.cleaned_data)
            return render(request,'django-form.html',{'form':form})
    
    else:
        form = contact()
        
    form = contact()
    return render(request,'django-form.html',{'form':form})
  

    
def newform(request):
    if request.method =='POST':
        form = new(request.POST,request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            print(form.cleaned_data)
            with open('./form_app/uploadfile/'+file.name,'wb+') as des:
                for chunk in file.chunks():
                    des.write(chunk)
            return render(request,'practiceform.html',{'form':form})
    else:
        form = new()
        
 
    return render(request,'practiceform.html',{'form':form})
  
        
        
        
def studentForm(request):
   
    if request.method == 'POST':
        
        form = s_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
    else:
        form = s_form()
    return render(request,'student.html',{'form':form})


def pas (request):
    if request.method == 'POST':
        
        form =password_project(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
                
    else:
        form = password_project()
        
    return render(request,'pass.html',{'form':form})