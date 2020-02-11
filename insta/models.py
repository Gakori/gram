from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from pyuploadcare.dj.models import ImageField

class Post(models.Model):
    '''
    class that defines the post content
    '''
    title = models.CharField(max_length=50)
    photo = ImageField(blank=True, manual_crop="")
    date_posted = models.DateField(default=timezone.now)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)  
    
    def __str__(self):
        return self.title

    
class Profile(models.Model):
    '''
    class that defines the user profile
    '''
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    followers = models.ManyToManyField(User, related_name='followers', blank='True')
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
class Comment(models.Model):
    '''
    class that defines how comments of the post are to be saved
    '''
    body = models.CharField(max_length=1000)
    image_id=models.ForeignKey(Post, on_delete=models.CASCADE)
    posted_by=models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateField(default=timezone.now)
    def __str__(self):
        return self.body
    
    
 