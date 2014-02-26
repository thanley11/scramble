from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    
    def __unicode__(self):
        return self.user.username
        
class Course(models.Model):
	name 		= models.CharField(max_length=128, unique=True)
	par         = models.IntegerField(default=0)
	handicap 	= models.IntegerField(default=0)
	location 	= models.CharField(max_length=128, default=None, blank=True)
	
	def __unicode__(self):
		return self.name
