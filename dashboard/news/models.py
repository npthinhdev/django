from django.db import models
from django.contrib.auth import get_user_model

class HeadLine(models.Model):
    title = models.CharField(max_length=120)
    image = models.ImageField()
    url = models.TextField()

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    last_scrape = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user}-{self.last_scrape}'
