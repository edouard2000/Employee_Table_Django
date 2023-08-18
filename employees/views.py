from django.shortcuts import get_object_or_404, render
from employees.models import Employees

def employees_detail(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    context = {
        "employee": Employee  
    }
    return render(request, "employee.html", context)

