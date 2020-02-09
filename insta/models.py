from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    '''
    class that defines the post content
    '''
    title = models.CharField(max_length=50)
    image=models.ImageField(upload_to='images')
    date_posted = models.DateField(default=timezone.now)
    
    def __str__(self):
        return self.title
    
class Profile(models.Model):
    '''
    class that defines the user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    
    def __str__(self):
        return f'{self.user.username} Profile'