from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'shop/index.html')

def about(request):
    return HttpResponse('We are at about us..')

def contact(request):
    return HttpResponse("We are at contact Us")

def productview(request):
    return HttpResponse('we are at product view')

def search(request):
    return HttpResponse("Please search anything you want.")

def checkout(request):
    return HttpResponse("checkout the listed items.")