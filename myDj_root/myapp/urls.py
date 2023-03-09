from django.urls import path

from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='home'),
    path('uploads', views.uploads, name='uploads')
]