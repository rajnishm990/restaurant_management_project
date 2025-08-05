from django.db import models

# Create your models here.

class Contact(models.Model):
  ''' Custom model or storing info of users Who contact us '''
  name = models.CharField(max_length =100)
  email =  models.EmailField()

