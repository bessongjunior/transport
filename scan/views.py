from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
# from django_barcode.views import BarcodeScannerView
from .forms import BarcodeForm

@login_required
def scanner(request):
    '''scanner endpoints/ page to scan and display data'''

    # return render(requmbest, 'scan/scan.html')
    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            barcode_data = form.save(commit=False)
            barcode_data.user = request.user
            barcode_data.save()
            # return render(request, 'success.html')
            redirect('home') 
    else:
        form = BarcodeForm()
    return render(request, 'scan/scan.html', {'form': form})

@login_required
def saveData(request):
    '''endpoint / view to save barcode data'''

    if request.user.is_authenticated:
#         # Get the current authenticated user.
        _user = request.user

    if request.method == 'POST':
        form = BarcodeForm(request.POST)
        print(form.is_valid())
        if form.is_valid():
            barcode_data = form.save(commit=False)
            barcode_data.user = _user
            barcode_data.save()
            # return render(request, 'success.html')
            redirect('home') 
    else:
        redirect('scanner')

@login_required
def success(request):
    return render(request, 'scan/success.html')

# def get_user_location(request):
#     if request.user.is_authenticated:
#         # Get the current authenticated user.
#         user = request.user
#         user_location = request.user.geolocation

#         # Saving the user's location in the database.
#         UserLocation.objects.create(
#             user=user,
#             longitude=user_location.longitude,
#             latitude=user_location.latitude,
#         )



# def getBarcodeData(request):
#     if request.method == 'POST':
#         form = BarcodeForm(request.POST)
#         if form.is_valid():
#             barcode_data = form.save(commit=False)
#             barcode_data.user = request.user
#             barcode_data.save()
#             # return render(request, 'success.html')
#             redirect('home')
#     else:
#         form = BarcodeForm()
#     return render(request, 'scan.html', {'form': form})

