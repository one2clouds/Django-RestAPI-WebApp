# Django-RestAPI-WebApp

1) After initializing your .venv or conda, ```pip install -r requirements.txt```

2) Create a new django project and make sure the project is up and running
```
django-admin startproject Company_API 
python Company_API/manage.py runserver 
```

3) Inside views create a new function for home_page then go into urls.py and map [views->function you wrote] with url [/url_name/]

4) Inside Company_API/settings add in installed apps section add 'rest_framework' for crud operations 

5) Create a startapp inside the main Company_API folder 
```
python Company_API/manage.py startapp API
``` 

6) Inside API/models Create models for conpany

7) Inside API/serializers create serializers for company

8) Inside API/views create CompanyViewset class which connects queryset and serializer class

9) Inside API/urls connect urls with viewset so that they are mapped together

10) Inside main urls file, i.e Company_API/urls add path and include(your_app.urls)
```
python Company_API/manage.py makemigrations
python Company_API/manage.py migrate
```
migration files acts as record of change to your database schema

11) Up to this step we have made a crup operation for company API

12) Then, make models for Employee, and add a foreign key of their company. For future reference between company and their employee. 
```
python Company_API/manage.py makemigrations
python Company_API/manage.py migrate
```

13) Inside API/serializers, create a class  employeeserializer and pass our model Employee

14) Then create viewset for employee, inside API/views. Inside API/urls using router, defaultrouter register the url and map url with viewset. Up to this step we have made a crup operation for employee API

15) Making a custom api for listing all employees inside a company 
``` companies/{companyId}/employees```
Inside API/views create a new function employees which gets primary key of employee from Company object, then filter employee from that primary key, then the filtered employees with employee serializers, and in context, pass {'request':request} as a dictionary. Then return emps._serializers.data as a Response. 

16) Inside Company_API/settings if you want user to authenticate then, inside REST_FRAMEWORK add 'DEFAULT_PERMISSION_CLASSES' section. Similarly, to off the browsable API, inside REST_FRAMEWORK add 'DEFAULT_RENDERER_CLASSES' section.

17) Inside API/admin register the Company and Employee 

18) Then, Create username and password
```
python Company_API/manage.py createsuperuser
python Company_API/manage.py runserver
```

19) Also, add CompanyAdmin for customizable section to display name and location of company. And add searchfields. And add searchfield. 

20) Then add EmployeeAdmin for customizable section to display name, email and company of employee, Then filter the employee list  companywise





