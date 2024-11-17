
from django.urls import path,include
from .views import authView,home

urlpatterns = [
    path('', authView, name="authView"),
    path("home", home, name="home"),
    path('accounts/', include("django.contrib.auth.urls"))
]