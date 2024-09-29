from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPES = [
        ('Car', 'Car'),
        ('Truck', 'Truck'),
        ('SUV', 'SUV'),
        # Add more vehicle types as needed
    ]

    FUEL_TYPES = [
        ('Petrol', 'Petrol'),
        ('Diesel', 'Diesel'),
        ('Electric', 'Electric'),
        # Add more fuel types as needed
    ]

    GEARBOX_TYPES = [
        ('Manual', 'Manual'),
        ('Automatic', 'Automatic'),
        # Add more gearbox types if necessary
    ]

    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50, choices=VEHICLE_TYPES)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    first_registration = models.CharField(max_length=10)
    mileage = models.CharField(max_length=20)
    fuel = models.CharField(max_length=20, choices=FUEL_TYPES)
    engine_size = models.CharField(max_length=20)
    power = models.CharField(max_length=20)
    gearbox = models.CharField(max_length=20, choices=GEARBOX_TYPES)
    num_seats = models.CharField(max_length=5)
    doors = models.CharField(max_length=5)
    color = models.CharField(max_length=20)
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.make} {self.model} ({self.type})'
