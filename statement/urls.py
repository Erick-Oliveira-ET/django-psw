from django.urls import path
from . import views

urlpatterns = [
    path('value/create', views.create_value, name="create_value")
]