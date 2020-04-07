from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from django.db.models.signals import post_save

# Create your models here.
app_name = 'core'





class Post(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	slug = models.SlugField()
	title = models.CharField(max_length=150)
	content = models.TextField()
	video = models.FileField(upload_to='blogpost_files/', blank=True, null=True)
	image1 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	image2 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	image3 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	image4 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	image5 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	image6 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	image7 = models.ImageField(upload_to='blogpost_files/', blank=True, null=True)
	timestamp = models.DateTimeField(auto_now_add=True)


	def __str__(self):
		return self.title


	def get_absolute_url(self):
		return reverse("core:post-detail", kwargs={"slug": self.slug})



class Aboutme(models.Model):
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	aboutme = models.TextField()

	def __str__ (self):
		return self.user.username


class Contact(models.Model)	:
	user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
	name = models.CharField(max_length=200)
	email = models.EmailField(max_length=80)
	number = models.IntegerField()
	message = models.TextField()


	def __str__ (self):
		return self.email		




class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.text		