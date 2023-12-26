from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone


class RoomMate(models.Model):

    class Level(models.TextChoices):
        HUNDRED_LEVEL = '1L', '100 Level'
        TWO_HUNRED_LEVEL = '2L', '200 Level'
        THREE_HUNDRED_LEVEL = '3L', '300 Level'
        FOUR_HUNDRED_LEVEL = '4L', '400 Level'
        FIVE_HUNDRED_LEVEL = '5L', '500 Level'
        
    class Religion(models.TextChoices):
        ISLAM = 'IS', 'Muslim'
        CHRISTIANITY = 'CR', 'Christian'
        OTHER = 'OT', 'Other'

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    searching = models.BooleanField(default=True)
    department = models.CharField(max_length=255, blank=True)
    level = models.CharField(max_length=2, choices=Level.choices, blank=True)
    religion = models.CharField(max_length=2, choices=Religion.choices, blank=True)
    about = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.user.username