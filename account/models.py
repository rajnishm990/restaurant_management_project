from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    ''' Custom profile model , extends User model  '''
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email =  models.EmailField(max_length=200)

    def __str__(self):
        return self.name if name else self.email

    
