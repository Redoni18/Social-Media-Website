from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from datetime import datetime


statusi = {
    ('Single','Single'),
    ('In a relationship', 'In a relationship'),
    ('Engaget','Engaget'),
    ('Married','Married'),
}

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.CharField(null= True, blank = True, max_length=50, verbose_name="Name: ")
    Bio = models.TextField(max_length=500, null= True, blank = True,verbose_name="Bio: ")
    birth_date = models.DateTimeField(default=datetime.now,verbose_name="Born on: ")
    statusi = models.CharField(max_length = 50, null= True, blank = True, choices=statusi)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    friends = models.ManyToManyField(User, related_name = "friends", blank = True)
    followers = models.ManyToManyField(User, related_name = "followers", blank = True)

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
    	super().save(*args, **kwargs)

    def total_friends(self):
    	return self.friends.count()

    def total_followers(self):
        return self.followers.count()


class Chat(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = "user",  null= True, blank = True)
    message = models.CharField(max_length=200)

    def __unicode__(self):
        return self.message