from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib import messages


from .models import WasteImage
from .forms import WasteImageForm

# Create your views here.

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



@login_required
def home(request):
    return render(request, 'home.html', {})

def authView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('accounts:login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {"form":form})


    
# Create your views here.
def upload_image(request):
    if request.method == 'POST':
        form = WasteImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Image uploaded sucessfully!")
            return redirect('accounts:blog')
    else:
        form = WasteImageForm()
    return render(request, 'upload.html', {'form': form})

def blog(request):
    images = WasteImage.objects.all().order_by('-created_at')
    return render(request, 'services/blog.html', {'images': images})



def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def account(request):
    return render(request, "account.html")

def educational(request):
    return render(request, "templates/educational.html")
