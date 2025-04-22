
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='index' ),
    path('home/',views.home,name='home' ),

    path('register/',views.register,name='register' ),
    path('profile/',views.profile,name='profile' ),
    path('logout/',views.login, name='logout' ),

    path('index/',views.login, name='login' ),
    path ('job_list/',views.login, name='job_list' ),
    path('about/',views.about,name='about' ),
    path('contact/',views.contact,name='contact' ),
    path('company/',views.company,name='company' ),
    path('job_create/',views.job_create,name='job_create' ),
    path('applicant/',views.applicant,name='applicant' ),
    path('job/',views.job,name='job' ),


]