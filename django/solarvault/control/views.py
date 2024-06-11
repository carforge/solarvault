from django.conf import settings
from django.shortcuts import render
from hanmatek import HM3xxP

set_dict = {}

# Create your views here.
def index(request):
    if request.method == "POST":
        psu = HM3xxP(settings.MY_PSU.interface)
        set_dict.update({
            "voltage":request.POST["voltage"], 
            "current": request.POST["current"]
            })

        if "psu_output" in request.POST:
            set_dict.update({
            "output":True
            })
        else:
            set_dict.update({
            "output":False
            })
        psu.write("voltage:set", set_dict["voltage"])
        psu.write("current:set", set_dict["current"])
        psu.write("output", set_dict["output"])

        return render(request, "control/index.html", {
            "psu": psu.info(),
            "voltage": set_dict["voltage"],
            "current": set_dict["current"],
            "output": set_dict["output"]
        })
    
    try:
        psu = HM3xxP(settings.MY_PSU.interface)
    except Exception:
        message = "Failed to initialise serial port. Go to settings."
        return render(request, "control/index.html", {
            "message": message
        })
    else:
        return render(request, "control/index.html", {
            "psu": psu.info(),
            "voltage": psu.read("voltage"),
            "current": psu.read("current"),
            "output": psu.read("output")
        })