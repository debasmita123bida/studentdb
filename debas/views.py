from django.shortcuts import render, get_object_or_404
from .models import Studentdb

def home (request):
    return render(request, 'debas/home.html')

def result(request):
    roll = request.POST.get('roll')
    data = get_object_or_404(Studentdb, rollno=roll)
    
    context = {
        'resultData' : data
    }
    return render(request, 'debas/result.html', context)