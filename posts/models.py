
import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	### links UserProfile to a User model instance.
	user = models.OneToOneField(User)

	# The additional attributes we wish to include.
	website = models.URLField(blank=True)


class User(models.Model):
	username = models.CharField(max_length=255, unique=True)
	password = models.CharField(max_length=255)
	access_token = models.UUIDField(default=uuid.uuid4)
	created_at = models.DateTimeField(default=timezone.now)
	updated_at = models.DateTimeField()
	
	def save(self, *args, **kwargs):
		self.updated_at = timezone.now()
		return super().save(*args, **kwargs)
		

class Post(models.Model):
	title = models.CharField(max_length=40)
	content = models.CharField(max_length=4000)
	slug = models.CharField(max_length=40, unique=True)
	created_at = models.DateTimeField(default=timezone.now, editable=False)
	updated_at = models.DateTimeField()

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = slugify(self.title)
		self.updated_at = timezone.now()
		return super().save(*args, **kwargs)







