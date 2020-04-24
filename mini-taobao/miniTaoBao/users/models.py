from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    is_seller = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
