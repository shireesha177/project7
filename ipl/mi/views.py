from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def rohit(request):
    return HttpResponse('<h1>rohit is captain of mi</h1>')


