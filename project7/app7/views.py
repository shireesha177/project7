from django.shortcuts import render

# Create your views here.
def happy(request):
    return render(request, 'hbd.html')
