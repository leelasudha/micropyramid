from django.db import models

# Create your models here.
class Employee(models.Model):
	fname = models.CharField(max_length=100)
	lname = models.CharField(max_length=100)
	email = models.EmailField()
	mobile= models.CharField(max_length=10)
	def __str__(self):
		return self.fname