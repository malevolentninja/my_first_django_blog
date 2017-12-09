from django.db import models

# Create your models here.

from django.db import models
from django.utils import timezone

# defines our model named Post, always start class with capital
class Post(models.Model): # (models.Model) = Post is a Django Model to save to database
  author = models.ForeignKey('auth.User')
  title = models.CharField(max_length=200)
  text = models.TextField()
  created_date = models.DateTimeField(default=timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def _str_(self):
    return self.title

