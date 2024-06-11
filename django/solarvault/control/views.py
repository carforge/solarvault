from django.http import HttpResponse
from django.shortcuts import render
from common.device import psu_device

# Create your views here.
def index(request):
    if request.method == "POST":
        device = psu_device(request.POST["device"])
        return render(request, "control/index.html", {
        "device": device
        })

    return render(request, "control/index.html")