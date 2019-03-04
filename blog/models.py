from django.db import models
from django.contrib.auth.models import  User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

class Image(models.Model):
    title = models.CharField(max_length=100)
    actor = models.CharField(max_length=100)
    picture = models.FileField(upload_to='images/pics/')

    def __str__(self):
        return self.title

