from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('add/', views.add_employee, name='add_employee'),  # Add employee page
    path('manage/', views.manage_employees, name='manage_employees'),  # Manage employees page
    path('update/<int:id>/', views.update_employee, name='update_employee'),  # Update employee
    path('delete/<int:id>/', views.delete_employee, name='delete_employee'),  # Delete employee
]
