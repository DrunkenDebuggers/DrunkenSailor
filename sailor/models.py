from django.db import models
from django.contrib.auth.models import User,Group

# Create your models here.

class Label(models.Model):
	name=models.CharField(max_length=32,unique=True,null=False,blank=False)
	color=models.CharField(max_length=6,default="FFFFFF",null=False,blank=False) # TODO create ColorField

	def __str__(self):
		return self.name

class Project(models.Model):
	title=models.CharField("Title",max_length=255,null=False,blank=False)
	active=models.BooleanField("Active",default=True,null=False)
	description=models.TextField(null=False,blank=False)
	label=models.ForeignKey(Label,blank=True)
	creator=models.ForeignKey(User,null=False,blank=False)
	solution_url=models.URLField(default=None,blank=True,null=True)
	solved=models.ForeignKey(Group,default=None,blank=True,null=True)

	def __str__(self):
		return self.title
