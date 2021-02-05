from django.db import models

# Create your models here.
class Url(models.Model):
    url= models.URLField()
    word1 = models.CharField(max_length=50)
    freq1 = models.PositiveIntegerField()
    word2 = models.CharField(max_length=50)
    freq2 = models.PositiveIntegerField()
    word3 = models.CharField(max_length=50)
    freq3 = models.PositiveIntegerField()
    word4 = models.CharField(max_length=50)
    freq4 = models.PositiveIntegerField()
    word5 = models.CharField(max_length=50)
    freq5 = models.PositiveIntegerField()
    word6 = models.CharField(max_length=50)
    freq6 = models.PositiveIntegerField()
    word7 = models.CharField(max_length=50)
    freq7 = models.PositiveIntegerField()
    word8 = models.CharField(max_length=50)
    freq8 = models.PositiveIntegerField()
    word9 = models.CharField(max_length=50)
    freq9 = models.PositiveIntegerField()
    word10 = models.CharField(max_length=50)
    freq10 = models.PositiveIntegerField()
    def __str__(self):
        return self.url