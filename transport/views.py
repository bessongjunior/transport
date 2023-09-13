from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def index(request):
    '''return app home page'''

    return render(request, 'transport/index.html')

@login_required(login_url='/accounts/login')
def home(request):
    '''redirects our user to scan'''

    return redirect(request, 'scan')