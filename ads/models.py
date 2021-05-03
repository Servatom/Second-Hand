from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

from users.models import CustomUser
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    price = models.IntegerField(blank=False)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='uploads', default='')

    def __str__(self):
        return f"{self.title}"

    def save(self):
        super().save()
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

    # def get_absolute_url(self):
    #     return reverse('post-detail', kwargs={'pk':self.pk})
