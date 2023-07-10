from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bill, name="view_bill"),
    path('create_bill/', views.create_bill, name="create_bill"),
    path('pay_bill/<int:id>', views.pay_bill, name="pay_bill"),
]