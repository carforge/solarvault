from django import forms
from django.http import HttpResponse
from django.shortcuts import render
from common.device import psu_device
import serial
import serial.tools
import serial.tools.list_ports


# Create your views here.
def index(request):
    if request.method == "POST":
        if not request.POST["device"] == None:
            device = psu_device(request.POST["device"])
            return render(request, "settings/settings.html", {
                "selected_device": device
            })
    
    serial_devices = serial.tools.list_ports.comports()
    return render(request, "settings/settings.html", {
        "devices": serial_devices
    })