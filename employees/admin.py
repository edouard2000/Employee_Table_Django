from django.contrib import admin
from .models import Employees

## Connect model to admin panel
admin.site.register(Employees)
