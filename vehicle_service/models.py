from django.db import models

class Component(models.Model):
    name = models.CharField(max_length=255)
    repair_price = models.DecimalField(max_digits=10, decimal_places=2)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    license_plate = models.CharField(max_length=50, unique=True)
    model = models.CharField(max_length=255)

    def __str__(self):
        return self.license_plate

class Issue(models.Model):
    NEW = 'new'
    REPAIR = 'repair'
    ISSUE_TYPE_CHOICES = [(NEW, 'New'), (REPAIR, 'Repair')]

    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    issue_type = models.CharField(max_length=10, choices=ISSUE_TYPE_CHOICES)

    def get_price(self):
        return self.component.purchase_price if self.issue_type == 'new' else self.component.repair_price

    def __str__(self):
        return f"{self.issue_type} for {self.component.name} on {self.vehicle.license_plate}"
