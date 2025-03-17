from django.db import models

# Create your models here.
# Creating company model 

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(("Research Company", "NAAMII"), ("Software Company", "NAAMCHE"), ("Non-tech", "Hotel")))
    added_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    # Shows the name of the company and not things like : Company Object (1)
    def __str__(self):
        return self.name + "---" + self.location

# Employee Model 
class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    about = models.TextField()
    position = models.CharField(max_length=100, choices=(
        ("Program Manager", "program_manager"),
        ('Software Developer', "software_developer"),
        ("Project Lead", "project_lead")
    ))
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



