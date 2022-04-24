from django.shortcuts import render

# Create your views here.

def index(request):                            #Index method that return index.html
    return render(request,"index.html")

