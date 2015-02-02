from django.db import models
from django.contrib.auth.models import User

class College(models.Model):

	meals = models.IntegerField(default=0)
	menu = models.CharField(max_length=128, default=' ')

	class Meta:
		abstract = True


class Swarthmore_Service(College):
	
	specialty = models.CharField(max_length=128, default=' ')
	homestyle = models.CharField(max_length=128, default=' ')
	vegetarian = models.CharField(max_length=128, default=' ')
	def __unicode__(self):
		return 'Swarthmore College'

class Haverford_Service(College):
	
	bar1 = models.CharField(max_length=128, default=' ')
	bar2 = models.CharField(max_length=128, default=' ')
	def __unicode__(self):
		return 'Haverford College'

class Consumer(models.Model):
    #Link consumer to user
    user = models.OneToOneField(User)
    
    #attributes
    name=models.CharField(max_length=128, default=' ')
    addressline1=models.CharField(max_length=128, default=' ')
    city=models.CharField(max_length=128, default=' ')
    zipcode=models.IntegerField(default=0)

    def __unicode__(self):
    	return self.user.username

class Driver(models.Model):

	user = models.OneToOneField(User)

	name = models.CharField(max_length=128, default=' ')
	phone = models.IntegerField(default=0)

	#1 corresponds to Swarthmore, 2 corresponds to Haverford
	SWAT = 'Swarthmore'
	HAVE = 'Haverford'
	SCHOOL_CHOICES = ((SWAT, 'Swarthmore'), (HAVE, 'Haverford'))
    
	school = models.CharField(max_length=10, choices=SCHOOL_CHOICES)

class Transaction(models.Model):

	#1 corresponds to Swarthmore, 2 corresponds to Haverford
	name = models.CharField(max_length=128, default=' ')

	SWAT = 'Swarthmore'
	HAVE = 'Haverford'
	SCHOOL_CHOICES = ((SWAT, 'Swarthmore'), (HAVE, 'Haverford'))
    
	school = models.CharField(max_length=10, choices=SCHOOL_CHOICES)

	consumer = models.ForeignKey(Consumer)

	drop_off = models.CharField(max_length=128, default=' ')
	city = models.CharField(max_length=128, default=' ')
	zipcode = models.IntegerField(default=0)


	date = models.DateTimeField()
	number_meals = models.IntegerField(default=1)

	def __str__(self):
		return self.school+' to '+self.drop_off+' at '+self.consumer.city+' on '+self.date.ctime()