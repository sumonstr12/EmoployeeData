from django import forms
from .models import Employee

# This form is used for adding a new employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'salary', 'designation', 'short_description']

# This form is used for updating employee details.
class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'address', 'phone_number', 'short_description']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set the readonly attribute for Salary and Designation
        self.fields['salary'] = forms.CharField(initial=self.instance.salary, disabled=True)
        self.fields['designation'] = forms.CharField(initial=self.instance.designation, disabled=True)
