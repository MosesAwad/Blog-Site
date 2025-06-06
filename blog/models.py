from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # Note 1

    def __str__(self): # Note 2
        return self.title
    
    def get_absolute_url(self): # Video part 10 at 28:08
        return reverse('post-detail', kwargs={'pk': self.pk})
