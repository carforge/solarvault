from django.http import HttpResponse
from django.shortcuts import render
import serial
import serial.tools
import serial.tools.list_ports

# Create your views here.
def index(request):
    if request.method == "POST":
          return HttpResponse("Hello!")
    
    serial_devices = serial.tools.list_ports.comports()#serial.tools.list_ports.comports()
    return render(request, "settings/settings.html", {
        "devices": serial_devices
    })