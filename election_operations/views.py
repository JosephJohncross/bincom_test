from django.shortcuts import render, redirect
from .models import AnnouncedPuResults, PollingUnit, Lga
from django.shortcuts import get_object_or_404

# Create your views here.

def home(request):
    lg = Lga.objects.all()
    context = {
        'lg': lg
    }
    return render(request, 'home.html', context)


def polling_unit_result(request):
    pu_number = request.GET.get("pu_number")
    if (pu_number):
        pu = get_object_or_404(PollingUnit, polling_unit_number=pu_number)
        pu_result = AnnouncedPuResults.objects.filter(polling_unit_uniqueid=pu.uniqueid)
    
        context = {
            'pu': pu,
            'pu_result': pu_result,
        }
        return render(request, 'polling_unit_result.html', context)
    else:
        return redirect("home")
    


def lga_result_from_pu(request):

    return render(request, 'lga_result_from_pu.html')

