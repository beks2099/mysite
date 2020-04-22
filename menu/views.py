from django.shortcuts import render
from . import models
# Create your views here.


def menu(request):
    context = {'menu': menu}
    return render(request, 'menu/menu.html', context)
