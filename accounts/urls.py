from django.urls import path,include
from .views import *
from . import views


from django.conf import settings
from django.conf.urls.static import static

app_name = 'accounts'  # This is essential when using namespaced URLs


urlpatterns = [
    path('', authView, name="authView"),
    path("home/", home, name="home"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('upload/', views.upload_image, name='upload_image'), 
    path('blog/', views.blog, name='blog'),


    path("about_us/", about_us, name="about_us"),
    path("consultation/", consultation, name="consultation"),
    path("contact_us/", contact_us, name="contact_us"),
    path("account/", account, name="account"),
    path("recycle/", recycle, name="recycle"),
    path("educational/", views.educational, name="educational"),


    # path('image/<int:image_id>/', views.image_detail, name='image_detail'),  # Add this line
    # path('visualization/<int:image_id>/', views.visualization, name='visualization'),  # Pass the image_id for individual image stats
    # path('like/<int:image_id>/', views.like_image, name='like_image'),

]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
