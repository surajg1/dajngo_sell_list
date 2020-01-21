from django.shortcuts import render

# Create your views here.
# 4:15:00

def home(request):
    return render(request, 'base.html')