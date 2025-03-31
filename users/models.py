from django.db import models

# Create your models here.
class User(models.Model):
  GENDER_CHOICES = [
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
  ]
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default='M')

  def __str__(self):
    return f"{self.first_name} {self.last_name}"