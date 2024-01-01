from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
from django.urls import reverse
from PIL import Image
from phonenumber_field.modelfields import PhoneNumberField


# User = get_user_model()

class UserAccount(AbstractUser):
    avatar = models.ImageField(default='-1homfs.jpg', upload_to='avatar/')
    phone_number = PhoneNumberField(blank=True)

    def is_roommate(self):
        return hasattr(self, 'roommate')


class Agent(models.Model):
    agent = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    about = models.TextField(blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    whatsapp = models.CharField(max_length=255, blank=True)
    instagram = models.CharField(max_length=255, blank=True)
    telagram = models.CharField(max_length=255, blank=True)
    facebook = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.agent.get_username()

    def get_absolute_url(self):
        return reverse('agent', args=[self.agent.username])
    