
from django.urls import path

from . import views

urlpatterns = [

    path('',views.home,name='index' ),
    path('about/',views.about,name='about' ),
    path('contact/',views.contact,name='contact' ),
    path('company/',views.company,name='company' ),
    path('applicant/',views.applicant,name='applicant' ),
    path('job/',views.job,name='job' ),
    path('job/<int:job_id>/',views.job_detail,name='job_detail' ),

    path('job/<int:job_id>/apply/',views.apply_job,name='apply_job' ),
    path('job/<int:job_id>/applications/',views.view_applications,name='view_applications' ),
    path('job/<int:job_id>/applications/<int:application_id>/',views.application_detail,name='application_detail' ),
    path('job/<int:job_id>/applications/<int:application_id>/accept/',views.accept_application,name='accept_application' ),
    path('job/<int:job_id>/applications/<int:application_id>/reject/',views.reject_application,name='reject_application' ),
    path('job/<int:job_id>/applications/<int:application_id>/delete/',views.delete_application,name='delete_application' ),
    path('job/<int:job_id>/applications/<int:application_id>/update/',views.update_application,name='update_application' ),
    path('job/<int:job_id>/applications/<int:application_id>/send_notification/',views.send_notification,name='send_notification' ),
    path('job/<int:job_id>/applications/<int:application_id>/send_notification/<str:status>/',views.send_notification,name='send_notification' ),
    path('job/<int:job_id>/applications/<int:application_id>/send_notification/<str:status>/<str:message>/',views.send_notification,name='send_notification' ),
   path('job/<int:job_id>/applications/<int:application_id>/send_notification/<str:status>/<str:message>/<str:recipient>/',views.send_notification,name='send_notification' ),



]