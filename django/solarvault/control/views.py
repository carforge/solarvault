from django.conf import settings
from django.shortcuts import render
from hanmatek import HM3xxP


# Create your views here.
def index(request):
    try:
        psu = HM3xxP(settings.MY_PSU.interface)
    except Exception:
        message = "Failed to initialise serial port"
        return render(request, "control/index.html", {
            "message": message
        })
    else:
        return render(request, "control/index.html", {
            "psu": psu.info(),
            "output": psu.read("output")
        })