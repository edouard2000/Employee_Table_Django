from django.shortcuts import get_object_or_404, render
from employees.models import Employees

def employees_detail(request, pk):
    Employee = get_object_or_404(Employees, pk=pk)
    context = {
        "Employee": Employee  
    }
    return render(request, "employee.html", context)

