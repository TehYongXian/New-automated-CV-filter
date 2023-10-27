from django.urls import path
from . import views

urlpatterns = [
    # path('readfile/', views.read_local_file, name='read_local_file'),
    path('', views.landing_page, name='landing_page'),
    path('readLocal', views.read_file, name='readLocal'),
    path('upload/', views.upload, name='upload'),


]
