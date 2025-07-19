from django.shortcuts import render, redirect
from .models import Vehicle
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm
@login_required


def sell_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            vehicle = form.save(commit=False)
            vehicle.seller = request.user
            vehicle.save()
            return redirect('buy_vehicle')
    else:
        form = VehicleForm()
    return render(request, 'vehicles/sell.html', {'form': form})


def buy_vehicle(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    return render(request, 'vehicles/buy.html', {'vehicles': vehicles})