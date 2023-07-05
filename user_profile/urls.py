
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('manage', views.manage, name="manage"),
    path('account/create', views.create_account, name="create_account"),
    path('category/create', views.create_category, name="create_category"),
]
