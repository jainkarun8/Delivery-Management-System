# views.py
from django.http import JsonResponse
from .models import Vehicle

def calculate_final_price(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(id=vehicle_id)
        issues = vehicle.issue_set.all()
        print("Vehicle:", vehicle.license_plate)
        for issue in issues:
            print("Issue:", issue, "Price:", issue.get_price())
        total_price = sum(issue.get_price() for issue in issues)
        print("Total Price:", total_price)
        return JsonResponse({'vehicle': vehicle.license_plate, 'total_price': total_price})
    except Vehicle.DoesNotExist:
        return JsonResponse({'error': 'Vehicle not found'}, status=404)
