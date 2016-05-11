from __future__ import unicode_literals
import datetime
from django.db import models
from django.utils import timezone


class Question(models.Model):
        question_text = models.CharField(max_length=200)
        pub_date = models.DateTimeField('date published')
        question_answer = models.CharField(max_length=300)
        def was_published_recently(self):
            return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
# Create your models here.
class Choice(models.Model):
        question = models.ForeignKey(Question)
        choice_text = models.CharField(max_length=200)
        votes = models.IntegerField(default=0)
