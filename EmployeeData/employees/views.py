from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm, EmployeeUpdateForm

# Home view to show all employees
def home(request):
    employees = Employee.objects.all()
    return render(request, 'employees/home.html', {'employees': employees})

# View to add a new employee
def add_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeForm()
    return render(request, 'employees/add_employee.html', {'form': form})

# View to manage employees
def manage_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees/manage_employees.html', {'employees': employees})

# Update employee view
def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == 'POST':
        form = EmployeeUpdateForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('manage_employees')
    else:
        form = EmployeeUpdateForm(instance=employee)
    return render(request, 'employees/update_employee.html', {'form': form})

# Delete employee view
def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('manage_employees')
