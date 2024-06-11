from django.shortcuts import render
from django.conf import settings
import serial.tools
import serial.tools.list_ports


# Create your views here.
def index(request):
    serial_devices = serial.tools.list_ports.comports()
    if request.method == "POST":
        settings.MY_PSU.mod_if(request.POST["device"])
        return render(request, "settings/settings.html", {
            "selected_device": settings.MY_PSU,
            "devices": serial_devices
        })
    
    return render(request, "settings/settings.html", {
        "selected_device": settings.MY_PSU,
        "devices": serial_devices
    })