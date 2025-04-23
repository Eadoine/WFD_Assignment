from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'edstaff/index.html')
def edstaff_list(request):
    return render(request, '')

def contact(request):
    return render(request, 'edstaff/contact.html')
def company(request):
    return render(request, 'edstaff/company.html')
def applicant(request):
    return render(request, 'edstaff/applicant.html')

def profile(request):
    return render(request, 'edstaff/profile.html')
def logout(request):
    return render(request, 'edstaff/logout.html')

def job_create(request):
    return render(request, 'edstaff/job_create.html')
def about(request):
    return render(request, 'edstaff/about.html')


def register_view(request):
    if request.method == 'POST':
        # Handle the registration logic here
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("posts:list")
    else:
        form = UserCreationForm()
    return render(request, 'edstaff/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        # Handle the login logic here
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Perform login
            return redirect("users:login")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})


def posts_list(request):

    return render (request, 'posts/posts_list.html')