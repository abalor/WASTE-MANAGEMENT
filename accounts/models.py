from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class WasteImage(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='waste_images/')
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name
