from django.db import models
from django.contrib.auth import get_user_model
from accounts.models import Agent
from django.utils import timezone
from django.urls import reverse
from django.core.validators import FileExtensionValidator
from django.utils.text import slugify
from django.utils.crypto import get_random_string
import locale
from cloudinary_storage.storage import VideoMediaCloudinaryStorage
from .validation import is_valid_video


# class PublishedManager(models.Manager):
#     def get_queryset(self) -> QuerySet:
#         return super().get_queryset().filter()

class Lodge(models.Model):

    class Campus(models.TextChoices):
        GK = 'GK', 'Gk'
        BOSSO = 'BS', 'Bosso'
    
    class Light(models.TextChoices):
        GENERAL_TRANSFORMER = 'GT', 'General Transformer'
        PRIVATE_TRANSFORMER = 'PT', 'Private Transformer'

    class Water(models.TextChoices):
        NO = 'NO', 'No'
        BOREHOLE = 'BH', 'Borehole'
        WELL = 'WL', 'Well'

    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    campus = models.CharField(max_length=2, choices=Campus.choices)
    area = models.CharField(max_length=50)
    available_rooms = models.IntegerField(default=0)
    cover_image = models.ImageField(default='11756.jpg', upload_to='lodge/', validators=[FileExtensionValidator(allowed_extensions=['jpg','png','jpeg',]),])
    water = models.CharField(max_length=2, choices=Water.choices)
    light = models.CharField(max_length=2, choices=Light.choices)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    description = models.TextField(blank=True)
    video = models.FileField(upload_to='videos/', blank=True,storage=VideoMediaCloudinaryStorage(),validators=[is_valid_video])
    created_at = models.DateTimeField(default=timezone.now)


    class Meta:
        ordering = ['-created_at']
        indexes = [models.Index(fields=['-created_at', 'name','campus','area','water','light','price',],)]
    
    def save(self, *args, **kwargs):
        # If the slug is not set or is empty, generate it from the name
        if not self.slug:
            base_slug = slugify(self.name)
            unique_slug = base_slug

            # Check for uniqueness and append a random string if needed
            while Lodge.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{get_random_string(4)}"

            self.slug = unique_slug

        super().save(*args, **kwargs)

    def formatted_price(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        formatted_price = locale.format('%0.2f', self.price, grouping=True)
        return formatted_price

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('lodge', args=[self.slug])


class LodgeImage(models.Model):
    image = models.ImageField(upload_to='lodges/',)
    lodge = models.ForeignKey(Lodge, on_delete=models.CASCADE, related_name='images')


class LodgeAmmenities(models.Model):
    ammenity = models.CharField(max_length=255)
    lodge = models.ForeignKey(Lodge, on_delete=models.CASCADE, related_name='ammenities')

    def __str__(self):
        return self.ammenity


class Room(models.Model):

    class RoomType(models.TextChoices):
        SELF_CONTAIN = 'SC', 'Self Contain'
        SINGE_ROOM = 'SR', 'Single Room'

    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    lodge = models.ForeignKey(Lodge, on_delete=models.CASCADE)
    type = models.CharField(max_length=2, choices=RoomType.choices)
    slug = models.SlugField(max_length=100)
    number = models.IntegerField(blank=True)
    block = models.CharField(max_length=50, blank=True)
    availabe = models.BooleanField(default=False)
    price = models.DecimalField(decimal_places=2, max_digits=9)
    cover_image = models.ImageField(default='11756.jpg', upload_to='rooms/',)
    video = models.FileField(upload_to='videos/', blank=True, storage=VideoMediaCloudinaryStorage(),validators=[is_valid_video])
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-created_at',]
        indexes = [models.Index(fields=['type','-created_at','price',],)]

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.lodge)
            unique_slug = base_slug

            # Check for uniqueness and append a random string if needed
            while Room.objects.filter(slug=unique_slug).exists():
                unique_slug = f"{base_slug}-{get_random_string(4)}"

            self.slug = unique_slug
        super().save(*args, **kwargs)

    def formatted_price(self):
        locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
        formatted_price = locale.format('%0.2f', self.price, grouping=True)
        return formatted_price

    def __str__(self):
        return self.lodge.name
    
    def get_absolute_url(self):
        return reverse('room', args=[self.slug])
    

class RoomImage(models.Model):
    image = models.ImageField(upload_to='rooms/',)
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='images')
    


