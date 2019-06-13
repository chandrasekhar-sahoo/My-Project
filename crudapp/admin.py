from django.contrib import admin
from crudapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
    list_display=['eno','ename','esal','eaddr']
    list_filter=['ename']
admin.site.register(Employee,EmployeeAdmin)    
