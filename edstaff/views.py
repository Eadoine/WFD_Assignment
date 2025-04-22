from django.shortcuts import render

def home(request):

    return render(request, 'edstaff/index.html')

def register(request):
    return render(request, 'edstaff/register.html')
def profile(request):
    return render(request, 'edstaff/profile.html')
def logout(request):
    return render(request, 'edstaff/logout.html')
def job_list(request):
    return render(request, 'edstaff/job_list.html')
def job_create(request):
    return render(request, 'edstaff/job_create.html')
def job_update(request):
    return render(request, 'edstaff/job_update.html')
def job_delete(request):
    return render(request, 'edstaff/job_delete.html')
def job_view(request):
    return render(request, 'edstaff/job_view.html')
def job_apply(request):
    return render(request, 'edstaff/job_apply.html')
def job_accept(request):
    return render(request, 'edstaff/job_accept.html')
def job_reject(request):
    return render(request, 'edstaff/job_reject.html')
def about(request):

    return render(request, 'edstaff/about.html')
def contact(request):
    return render(request, 'edstaff/contact.html')
def login(request):

    return render(request, 'edstaff/login.html')
def company(request):
    return render(request, 'edstaff/company.html')
def applicant(request):

    return render(request, 'edstaff/applicant.html')
def job(request):
    return render(request, 'edstaff/job.html')

