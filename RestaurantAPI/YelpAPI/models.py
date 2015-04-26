import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __unicode__(self):
    	return self.question_text

class Business(models.Model):
    Type = models.CharField(max_length=200)
    business_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    stars = models.FloatField()
    review_count = models.PositiveIntegerField()
    def __unicode__(self):
    	return unicode(self.stars)

