from django.db import models

# Create your models here.
class User(models.Model):
    firstName = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.firstName + ' ' + self.lastName
