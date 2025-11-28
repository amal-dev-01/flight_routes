from django.db import models

# Create your models here.

class Airport(models.Model):
    code = models.CharField(max_length=3, unique=True, db_index=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class AirportRoute(models.Model):
    LEFT = 'Left'
    RIGHT = 'Right'
    POSITION_CHOICES = [
        (LEFT, 'Left'),
        (RIGHT, 'Right'),
    ]

    from_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='from_routes' ,db_index=True)
    to_airport = models.ForeignKey(Airport, on_delete=models.CASCADE, related_name='to_routes', db_index=True)
    position = models.CharField(max_length=10, choices=POSITION_CHOICES)
    duration = models.PositiveIntegerField(db_index=True) 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('from_airport', 'to_airport')
    def __str__(self):
        return f"{self.from_airport.code} → {self.to_airport.code}"
