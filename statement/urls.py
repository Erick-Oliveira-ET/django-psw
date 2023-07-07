from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_statement, name="view_statement"),
    path('value/create', views.create_value, name="create_value")
]