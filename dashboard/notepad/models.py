from django.db import models
from django.contrib.auth import get_user_model

class Note(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    image = models.ImageField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_delete_url(self):
        return f'/note/{self.pk}/delete'

    def get_update_url(self):
        return f'/note/{self.pk}/update'
