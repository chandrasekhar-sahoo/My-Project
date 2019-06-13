from rest_framework.viewsets import ModelViewSet
from crudapp.models import Employee
from . serializers import EmployeeSerializer

class EmployeeApiView(ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
