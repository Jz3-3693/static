from django.shortcuts import render
def login(request):
    return render(request,'login.html')
def home(request):
    return render(request,'home.html')
def index(request):
    return render(request,'index.html')
# Create your views here.
