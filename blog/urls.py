from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('images/', views.image_list, name='image_list'),
    path('images/upload/', views.upload_image, name='upload_image'),
]
