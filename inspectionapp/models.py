from django.db import models
from django.contrib.auth.models import User

class House(models.Model):
	name = models.CharField(max_length=80)
	abbreviation = models.CharField(max_length=3)

	def __unicode__(self):
		return self.abbreviation

class Inspection(models.Model):
	time = models.DateTimeField(auto_now_add=True)
	house = models.ForeignKey(House)
	success = models.BooleanField()
	submit_by = models.ForeignKey(User)

	def __unicode__(self):
		mdy = ('/').join([str(self.time.month), str(self.time.day), str(self.time.year)])
		return mdy + ' ' + self.house.name
