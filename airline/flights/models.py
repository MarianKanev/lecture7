from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3)
    city = models.CharField(max_length=64)

    def __str__(self):
         return f"{self.city} ({self.code})"

# on_delete=models.CASCADE - means if we delete some Airport code all flights with that code will be deleted
class Flight(models.Model):
    origin = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="departures")
    destination =  models.ForeignKey(Airport, on_delete=models.CASCADE, related_name="arrivals")
    duration = models.IntegerField()


    def __str__(self):
        return f"{self.id} - {self.origin} to {self.destination}"

class Passenger(models.Model):
    first = models.CharField(max_length=64) # First Name
    last = models.CharField(max_length=64)  # Last Name
    flights = models.ManyToManyField(Flight, blank=True, symmetrical=False, related_name="passengers") # Passenger is linked to Flight. Link is ManytoMany
    
    def __str__(self):
        return f"{self.first} {self.last}"