
from django.urls import path

from . import views

urlpatterns = [

    path("form/",views.form,name='form'),
    path("about/",views.about,name='about'),
    path('djangoform/',views.Django_Froms,name='form_django'),
    path('practiceform/',views.newform,name='newform'),
    path('studentform/',views.studentForm,name='student'),
    path('password/',views.pas,name="pass")
   
]