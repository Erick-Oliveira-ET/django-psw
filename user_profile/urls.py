
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('manage', views.manage, name="manage"),
    path('account/create', views.create_account, name="create_account"),
    path('account/delete/<int:id>', views.delete_account, name="delete_account"),
    path('category/create', views.create_category, name="create_category"),
    path('category/update/<int:id>', views.toggle_category_essential, name="toggle_category_essential"),

]
