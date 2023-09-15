from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
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

# @login_required
# def success(request):
#     return render(request, 'scan/success.html')

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

# from django.shortcuts import render
# import cv2
# import threading
# from django.http import StreamingHttpResponse, HttpResponse
# from pyzbar.pyzbar import decode
# import time

# def indexapp(request):
#     return render(request, 'scan/webcam/home1.html')

# def homeapp(request):
#     try:
#         cam = VideoCamera()
#         return StreamingHttpResponse(gen(cam), content_type="multipart/x-mixed-replace;boundary=frame")
#     except:
#         pass
#     return render(request, 'scan/webcam/app1.html')

# def helloView(request, code):
#     http = f"Hello {code}"
#     return HttpResponse(http)

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         # n_1 = '9788366384088'
#         for code in decode(image):
#             n = str(code.data.decode('utf-8'))
#             # if n_1 == n:
#             #     print(n)
#             #     time.sleep(5)
#             print(n)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\\r\\n' b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n\\r\\n')


# from django.shortcuts import render
# from django.http import JsonResponse
# from pyzbar.pyzbar import decode
# import cv2
# import numpy as np
# import base64


# # jquery error

# def indexappa(request):
#     return render(request, 'scan/webcam/home.html')

# def read_barcode(request):
#     if request.method == 'POST':
#         dataUrl = request.POST['image']
#         encoded_data = dataUrl.split(',')[1]
#         nparr = np.fromstring(base64.b64decode(encoded_data), np.uint8)
#         img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
#         barcodes = decode(img)
#         if barcodes:
#             barcode_data = barcodes[0].data.decode("utf-8")
#             return JsonResponse({'barcode': barcode_data})
#         else:
#             return JsonResponse({'error': 'No barcode found'})


# def testapp(request):
#     return render(request, 'scan/webcam/app1.html')