from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def HomePage(request):
    return render(request, 'blog/index.html')

def Recommendation(request):
    return render(request, 'blog/recommendation.html')

def r_result(request):
    return render(request, 'blog/r_result.html')

def post(request):
    return render(request, 'blog/post.html')
    