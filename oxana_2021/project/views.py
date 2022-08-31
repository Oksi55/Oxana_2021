from django.shortcuts import render
from .models import Project

def project(request):
    return render(request,'prog.html')
