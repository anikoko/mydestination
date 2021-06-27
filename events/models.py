from django.db import models
from django.contrib.auth.models import User

class Venue(models.Model):
	name = models.CharField('Venue Name', max_length=300) 
	address =  models.CharField(max_length=300, blank=True)
	zip_code =  models.CharField('Zip Code', max_length=15, blank=True)
	phone =  models.CharField('Contact Phone', max_length=25, blank=True)
	web = models.URLField('Website Address', blank=True)
	email_address = models.EmailField('Email Address', blank=True)
	review = models.CharField('Your Reveiw', max_length=1000, blank=True)

	def __str__(self):
		return self.name

class MyClubUser(models.Model):
	firt_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	email = models.EmailField('User Email')

	def __str__(self):
		return self.firt_name + ' ' + self.last_name


class Event(models.Model):
	name = models.CharField('Events Name', max_length=120)
	event_date = models.DateTimeField('Event Date')
	venue = models.ForeignKey(Venue, blank=True, null=True, on_delete=models.CASCADE)
	#venue = models.CharField(max_lenght=120)
	manager = models.CharField(max_length=120, blank=True)  
	description = models.TextField(blank=True)
	attendees = models.ManyToManyField(MyClubUser, blank=True)

	def __str__(self):
		return self.name