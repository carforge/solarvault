from django.shortcuts import render
from hanmatek import HM3xxP

# Create your views here.
def read_data(request):
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
            return psu.read("power")