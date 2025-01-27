from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate_doc/', views.collect_credentials, name='generate_doc')
   
]
