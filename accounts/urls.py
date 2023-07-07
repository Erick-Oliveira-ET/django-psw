
from django.urls import path
from . import views

urlpatterns = [
    path('define_account/', views.define_account, name="define_account"),

]
