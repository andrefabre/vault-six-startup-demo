from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'base.html')

def dashboard(request):
    return HttpResponse("This is the dashboard view.")
    #return render(request, 'dashboard.html')

def assets(request):
    return HttpResponse("This is the assets view.")
    #return render(request, 'assets.html')

def requests(request):
    return HttpResponse("This is the requests view.")
    #return render(request, 'requests.html')
    
def review_queue(request):
    return HttpResponse("This is the review queue view.")
    #return render(request, 'review_queue.html')    