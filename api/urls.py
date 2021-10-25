from django.urls import path
from .views import index
from api import views

urlpatterns = [
    
    path('', views.index, name="home")
]
