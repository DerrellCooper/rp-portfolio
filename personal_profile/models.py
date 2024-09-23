from django.db import models

# Create your models here.

class Profile(models.Model):
    name = models.CharField(max_length=100)
    about_me = models.TextField()
    skills = models.TextField()
    phone = models.PositiveBigIntegerField()
    email = models.EmailField()
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    image = models.FileField(upload_to='profile_images', blank=True)