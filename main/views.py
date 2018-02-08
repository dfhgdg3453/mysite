from django.shortcuts import render
from django.http import HttpResponse

from django.utils import timezone


def IndexView(request):

    return render(request, 'main\index.html')