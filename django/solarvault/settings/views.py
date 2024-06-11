from django.shortcuts import render
from common.device import psu_device
import serial.tools
import serial.tools.list_ports

DEVICE = psu_device()

# Create your views here.
def index(request):    
    serial_devices = serial.tools.list_ports.comports()
    return render(request, "settings/settings.html", {
        "devices": serial_devices
    })