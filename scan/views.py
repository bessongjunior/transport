from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def scanner(request):
    '''scanner endpoints/ page to scan and display data'''

    return render(request, 'scan/scan.html')