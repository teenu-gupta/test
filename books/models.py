from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Book(models.Model):
	name = models.CharField(max_length=400,null=False,blank=False)
	author = models.CharField(max_length=300,blank=False,null=False)
	inventory_count = models.IntegerField(default=1)
	price = models.FloatField(default=0)

	def __unicode__(self):
		return str(self.name)


class Employee(models.Model):
	employee_name = models.CharField(max_length=400)
	team = models.CharField(max_length=400)

	def __unicode__(self):
		return str(self.employee_name)

class Book_Issue_Details(models.Model):
	book_status = (("True",_("Issued")),("False",_("In Library")))
	book = models.ForeignKey(Book)
	book_issued_to = models.ForeignKey(Employee,null=True,blank=True)
	status = models.CharField(max_length=200,choices=book_status,default=True)
	date_of_issue = models.DateField(auto_now=True)
	date_of_return = models.DateField(null=True,blank=True)

	def __unicode__(self):
		return "%s %s" %(self.book,self.book_issued_to)

	