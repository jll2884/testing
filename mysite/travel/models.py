from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class post(models.Model):  #creates an SQL  table
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default= timezone.now) #will automatically make the date when it is modified
    author = models.ForeignKey(User,on_delete= models.CASCADE) #deletes posts if user is deleted

    def __str__(self):
        return self.title

    def get_absolute_url(self): # redirects to detailed page of new created post
        return reverse('post-detail', kwargs={'pk': self.pk})

# Create your models here.
