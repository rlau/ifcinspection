from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=80)
	abbreviation = models.CharField(max_length=3)
	house1 = models.CharField(max_length=80)
	house2 = models.CharField(max_length=80)
	# phone1 = models.CharField(max_length=20)
	# phone2 = models.CharField(max_length=20)

	def __unicode__(self):
		return self.abbreviation

class Inspection(models.Model):

	time = models.DateTimeField(auto_now_add=True)
	date = models.DateField()
	house = models.ForeignKey(House)
	success = models.BooleanField()
	submit_by = models.ForeignKey(User)

	def __unicode__(self):
		mdy = ('/').join([str(self.date.month), str(self.date.day), str(self.date.year)])
		return mdy + ' ' + self.house.name
