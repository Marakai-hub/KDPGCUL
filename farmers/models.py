from django.db import models
from django.utils.crypto import get_random_string

def generate_farmer_id():
    return 'F' + get_random_string(8, allowed_chars='0123456789')

class Farmer(models.Model):
    farmer_id = models.CharField(
        max_length=10,
        unique=True,
        editable=True,
        default=generate_farmer_id
    )
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=10)
    age = models.IntegerField()
    land_size = models.DecimalField(max_digits=5, decimal_places=2)
    county = models.CharField(max_length=100)
    subcounty = models.CharField(max_length=100)
    parish = models.CharField(max_length=100)
    village = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        if not self.farmer_id:
            self.farmer_id = generate_farmer_id()
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Query(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    issue = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

class Harvest(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    season = models.CharField(max_length=20)
    land_size = models.DecimalField(max_digits=5, decimal_places=2)
    potato_kg = models.DecimalField(max_digits=5, decimal_places=2)
    date_reported = models.DateTimeField()

class PlantingReport(models.Model):
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    season = models.CharField(max_length=20)
    land_size = models.DecimalField(max_digits=5, decimal_places=2)
    potato_kg = models.DecimalField(max_digits=5, decimal_places=2)
    planting_date = models.DateField()

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    location = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.title} on {self.date}"
