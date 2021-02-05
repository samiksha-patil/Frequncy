from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


MODE = (
    ("Public", "Public"),
    ("Private", "Private"),
)

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    blog = models.TextField()
    date_posted= models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    image= models.ImageField(default='default.jpg',upload_to='post')
    mode= models.CharField(choices=MODE, max_length=7,default='public')
   
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})

class Answer(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='answers')
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    comment = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_answer = models.BooleanField(default=False)

    def approve(self):
        self.approved_answer = True
        self.save()

    def __str__(self):
        return self.author.username
    def get_absolute_url(self):
        return reverse('post-detail',kwargs={'pk': self.pk})