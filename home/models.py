from django.db import models

# Create your models here.

# makemigrations - create changes and store in a file
# migrate - apply the pending chnages created by make migrations

class Contact(models.Model):    #this  class contact means a table/excel sheet in database
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone=models.CharField(max_length=12)
    desc= models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.name        #to return name of person in database instead of anonymous