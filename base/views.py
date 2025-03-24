from django.shortcuts import render

def home(request):
    return render(request , "base/index.html")

def rank(request):
    return render(request , "base/rank.html")

def profile(request):
    return render(request , 'base/profile.html')