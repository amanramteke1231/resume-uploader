from django.db import models

# Create your models here.
STATE = [('mumbai', 'mumbai'),
         ('pune', 'pune'),
         ('chhattisgarh','chhattisgarh'),
         ('j&k','j&k'),]

class Resume(models.Model):
    fullname = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gander = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    state = models.CharField(choices=STATE, max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    mobile = models.PositiveIntegerField()
    email = models.EmailField(max_length=100)
    job_city = models.CharField(max_length=100)
    profile = models.ImageField(upload_to = 'profile', blank = True)
    myfile = models.FileField(upload_to = True, blank = True)



