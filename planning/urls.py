from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_planning, name="view_planning"),
    path('define_planning/', views.define_planning, name="define_planning"),
    path('update_value_category/<int:id>', views.update_value_category, name="update_value_category"),
]