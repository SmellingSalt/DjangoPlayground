from django.shortcuts import render
import time

# Create your views here.
def home(request):
    return render(request,"index.html")

def url_check(request):
    # url=request.GET["url"]
    render(request,"result.html")
    time.sleep(5)
    return render(request,"result.html")
    