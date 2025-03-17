from django.shortcuts import render
from rest_framework import viewsets
from API.models import Company, Employee
from API.serializers import CompanySerializer, EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    # companies/{company_id}/employees
    @action(detail=True, methods=['get'])
    def employees(self, request, pk=None):
        # pk, gives the promary key of the company, 
        try: 
            company = Company.objects.get(pk=pk) # it has the object of the company WITH Primary key=PK
            employee = Employee.objects.filter(company=company) # get employee of company with unique primary key at employee object 
            
            employee_serializers = EmployeeSerializer(employee, many=True, context={'request':request})
            return Response(employee_serializers.data)
        
        except Exception as e:
            print(e)
            return Response({
                'message': f'{e}'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
