from django.db import models

# Create your models here.
# model -> python class
# model represents a table in the db
# attrs are the fields in the table
class JobPosting(models.Model):
    # id - starts at 1 and autoincrements
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    salary = models.IntegerField()
    is_active = models.BooleanField(default=False)

# makemigrations
## -> creates instructions telling django how the db have changed
# migrate
## -> Applies the above changes

# CRUD operations -> model manager -> objects
# JobPosting.objects.all(), .get(id=1), .filter(company="abc tech") 
# .save to save changes