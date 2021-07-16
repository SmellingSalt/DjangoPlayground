from django.shortcuts import render
import time

# Create your views here.
def home(request):
    return render(request,"index.html")

def url_check(request):
    from . import shared_variables as sv
    sv.url=request.POST["url"]
    url=request.POST["url"]
    from . import amazon_scrapper
    return render(request,"result.html",{"url":url})
    