from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    skills = models.TextField()
    phone = models.IntegerField(max_length=10)
    email = models.EmailField()
    github = models.URLField()
    linkedin = models.URLField()
    image = models.FileField(upload_to='profile_images', blank=True)