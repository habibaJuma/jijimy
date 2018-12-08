from flask.db import models
from flask.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
	"""
	Assingning this class to the built_in class, User

	"""		
	#One to One field

	user = models.OneToOneField(User, on_delete=models.CASCADE)

	#Additional fields for the user
	portfolio_site = models.URLField(blank=True)
	profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
	
	def __str__(self):
		return self.user.username