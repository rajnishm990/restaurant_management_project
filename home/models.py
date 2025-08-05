from django.db import models

# Create your models here.

class MenuItem(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits = 10 , decimal_places=2)

    def __str__(self):
        return f"{self.name} - \n {self.description[:50]}"
        

class Contact(models.Model):
    name = models.CharField(max_length = 100)
    email =  models.EmailField()

    def __str__(self):
        return f"query by {self.name}"



