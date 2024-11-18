from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.contrib import messages


from .models import WasteImage
from .forms import *

from django.shortcuts import get_object_or_404

# Create your views here.


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
# @login_required
# def upload_image(request):
#     if request.method == 'POST':
#         form = WasteImageForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Image uploaded sucessfully!")
#             return redirect('accounts:blog')
#     else:
#         form = WasteImageForm()
#     return render(request, 'upload.html', {'form': form})

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = WasteImageForm(request.POST, request.FILES)
        if form.is_valid():
            waste_image = form.save(commit=False)  # Don't save to the database yet
            waste_image.user = request.user       # Associate the logged-in user
            waste_image.save()                    # Save to the database
            messages.success(request, "Image uploaded successfully!")
            return redirect('accounts:blog')
    else:
        form = WasteImageForm()
    return render(request, 'upload.html', {'form': form})

def blog(request):
    images = WasteImage.objects.all().order_by('-created_at')
    return render(request, 'services/blog.html', {'images': images})

# Blog page to display uploaded images and their associated likes and comments
# @login_required
# def blog(request):
#     waste_images = WasteImage.objects.all()

#     # Handle commenting
#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             comment = comment_form.save(commit=False)
#             comment.user = request.user
#             comment.save()
#             return redirect('accounts:blog')  # Assuming the blog page has URL 'accounts:blog'
#     else:
#         comment_form = CommentForm()

#     return render(request, 'blog.html', {
#         'waste_images': waste_images,
#         'comment_form': comment_form,
#     })


@login_required
def about_us(request):
    return render(request, "about_us.html")


def image_detail(request, image_id):
    image = get_object_or_404(WasteImage, id=image_id)
    return render(request, 'services/image_detail.html', {'image': image})


def contact_us(request):
    return render(request, "contact_us.html")

@login_required
def account(request):
    return render(request, "account.html")

@login_required
def educational(request):
    return render(request, "services/educational.html")

@login_required
def consultation(request):
    return render(request, "services/consultation.html")


@login_required
def recycle(request):
    return render(request, "services/recycle.html")


# @login_required
# def visualization(request, image_id):
#     image = get_object_or_404(WasteImage, id=image_id)
#     likes_count = image.likes.count()
#     comments_count = image.comments.count()
#     return render(request, 'services/visualization.html', {
#         'image': image,
#         'likes_count': likes_count,
#         'comments_count': comments_count,
#     })




@login_required
def like_image(request, image_id):
    waste_image = get_object_or_404(WasteImage, id=image_id)
    
    if request.user in waste_image.likes.all():
        waste_image.likes.remove(request.user)
    else:
        waste_image.likes.add(request.user)
    
    return redirect('accounts:blog')  # Redirect back to the blog page
