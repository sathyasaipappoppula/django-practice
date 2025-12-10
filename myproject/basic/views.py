from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def service(request):
    return render(request,'service.html')
def sample1(request):
    q1=request.GET.get("name")
    q2=request.GET.get("city")
    return HttpResponse(f"{q1} came from {q2}")

