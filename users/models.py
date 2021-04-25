from django.db import models

from django.contrib.auth.models import User

# Proxy model
class Customer(User): # Para agregar funcionalidad a User
    class Meta:
        proxy = True

    def get_products(self):
        return []

class Profile(models.Model): # Para agregar campos a un modelo relacion One to One
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
