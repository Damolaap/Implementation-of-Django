from django.db import models

#RDBMS They store data in rows and columns Relational database management system
#sql structured query language
#No sql means not only sql so it can also store non structured data
# ORM object relational mapper: interpreter betweem python and database
#working sql lite...
#every model that is created translates to a database

# Create your models here.

#every model created has to be a class

#creating tables
#CRUD 
# Create 
# Read: rows and columns BioData.objects.all(), BioData.objects.filter(name = ...), BioData.objects.get(name= ...)
#.first, .last for all() and filter() 
# Update
# Delete 
# relationships between objects: One-to-one, One-to-many(foreign key), Many-to-Many

class BioData(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female'), ('NB', 'Non binary')]
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    age = models.IntegerField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='M')

    def __str__(self):
        return (f'{self.fname}-{self.lname}')
    

class BlogData(models.Model):
    post_title = models.CharField(max_length=400)
    post_body = models.TextField()
    #date_posted = models.DateField(auto_now_add=True)
    date_posted = models.DateField()

class Person(models.Model):
    about = models.TextField()
    data = models.OneToOneField(BioData, on_delete=models.CASCADE)

    def __str__(self):
        return (f'Person{self.id}')
    
#




#choices field : a list of tuple or a tuple of tuples
    

# make migratiions
# migrate, to be transferred to database
#.makemigration
#.migrate
#to see all the rows in the model use the modelname.objects.all()