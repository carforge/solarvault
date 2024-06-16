from django.conf import settings
from django.shortcuts import render
from hanmatek import HM3xxP

# Create your views here.
def psu_control(request):
    if len(request.GET) > 0:
        interface = request.GET['if']
        try:
            psu = HM3xxP(interface)
        except Exception:
            message = "Failed to initialise serial port. Choose another Serial Interface."
            return render(request, "control/control.html", {
                "message": message
            })
        else:
            # Check if voltage is a numerical value
            try:
                if 0 <= float(request.GET['v']) <= 32:
                    voltage = request.GET['v']
            except Exception:
                psu.write("output", False)
                message = "Voltage is not a numerical value or out of range."
                return render(request, "control/control.html", {
                    "message": message
                })
            # Check if current is a numerical value
            try:
                if 0 <= float(request.GET['c']) <= 5:
                    current = request.GET['c']
            except Exception:
                psu.write("output", False)
                message = "Current is not a numerical value."
                return render(request, "control/control.html", {
                    "message": message
                })
            # Check if output is a boolean value
            if request.GET['o'].lower() == "true" or request.GET['o'].lower() == "false":
                current = request.GET['o']
            else:
                psu.write("output", False)
                message = "Output is not a boolean value."
                return render(request, "control/control.html", {
                    "message": message
                })
            
            current = request.GET['c']
            output = request.GET['o'].capitalize()
            psu.write("voltage:set", voltage)
            psu.write("current:set", current)
            psu.write("output", output)
            return render(request, "control/control.html", {
                "interface": f"Interface: {interface}",
                "voltage": f"Voltage: {voltage} [V]",
                "current": f"Current: {current} [A]",
                "output": f"Output ON: {output}"
            })
    else:
        message = "No PSU defined. Go to settings or use settings paramters in URL."
        return render(request, "control/control.html", {
            "message": message
        })