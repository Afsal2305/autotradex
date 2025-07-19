from django.shortcuts import render, redirect
from .models import Vehicle
from django.contrib.auth.decorators import login_required

@login_required
def sell_vehicle(request):
    if request.method == 'POST':
        title = request.POST['title']
        brand = request.POST['brand']
        price = request.POST['price']
        year = request.POST['year']
        description = request.POST['description']
        image = request.FILES['image']
        Vehicle.objects.create(
            seller=request.user,
            title=title,
            brand=brand,
            price=price,
            year=year,
            description=description,
            image=image
        )
        return redirect('buy_vehicle')
    return render(request, 'vehicles/sell.html')

def buy_vehicle(request):
    vehicles = Vehicle.objects.all().order_by('-created_at')
    return render(request, 'vehicles/buy.html', {'vehicles': vehicles})
