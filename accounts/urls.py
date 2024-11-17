from django.urls import path,include
from .views import *
from . import views

app_name = 'accounts'  # This is essential when using namespaced URLs


urlpatterns = [
    path('', authView, name="authView"),
    path("home/", home, name="home"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('upload/', views.upload_image, name='upload_image'), 
    path('blog/', views.blog, name='blog'),


    path("about_us/", about_us, name="about_us"),
    path("contact_us/", contact_us, name="contact_us"),
    path("account/", account, name="account"),
    path("educational/", views.educational, name="educational"),

]