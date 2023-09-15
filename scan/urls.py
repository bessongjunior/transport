from django.urls import path
from . import views

urlpatterns = [
    path('', views.scanner, name='scanner'),
    path('scanned/', views.saveData, name='savedata'),
    # path('success/', views.success, name='success'),

    # path('index/', views.indexappa, name='indexappa'),
    # path('home/', views.read_barcode, name='read_barcode'),
    # path('testapp/', views.testapp, name='testapp')
]