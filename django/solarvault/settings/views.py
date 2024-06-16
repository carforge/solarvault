from django.shortcuts import render
import serial.tools
import serial.tools.list_ports


# Create your views here.
def index(request):
    serial_devices = serial.tools.list_ports.comports()
    
    return render(request, "settings/settings.html", {
        "devices": serial_devices
    })