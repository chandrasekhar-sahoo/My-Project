from rest_framework.serializers import ModelSerializer
from crudapp.models import Employee

class EmployeeSerializer(ModelSerializer):
    class Meta:
        model=Employee
        fields='__all__'
