from django.test import TestCase
from .models import Component, Vehicle, Issue

class PriceCalculationTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle.objects.create(license_plate="ABC123", model="Sedan")
        self.component = Component.objects.create(name="Engine", repair_price=500, purchase_price=1000)
        Issue.objects.create(vehicle=self.vehicle, component=self.component, issue_type="repair")

    def test_price_calculation(self):
        response = self.client.get(f'/calculate-price/{self.vehicle.id}/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['total_price'], 500)
