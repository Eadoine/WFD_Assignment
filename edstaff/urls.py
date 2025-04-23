from idlelib.pathbrowser import PathBrowser

from django.urls import path

from . import views

urlpatterns = [
    path ('', views.posts_list, name='posts_list'),
    path('',views.home,name='index' ),
    path('',views.home,name='homepage' ),
    path('register/',views.register_view,name='register' ),
    path('profile/',views.profile,name='profile' ),
    path('logout/',views.logout, name='logout' ),
    path('login/',views.login_view, name='login' ),
    path('about/',views.about,name='about' ),
    path('contact/',views.contact,name='contact' ),
    path('company/',views.company,name='company' ),
    path('job_create/',views.job_create,name='job_create' ),
    path('applicant/',views.applicant,name='applicant' ),

]