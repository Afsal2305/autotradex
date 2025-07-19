from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    year = models.IntegerField()
    description = models.TextField()
    image = models.ImageField(upload_to='vehicle_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
