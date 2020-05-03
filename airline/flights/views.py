from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from . models import Flight     # Import Flight class from the models in current directory

# Create your views here.

def index(request):
#    return HttpResponse("Flights")
    context = {
        "flights": Flight.objects.all()
    }
    return render(request, "flights/index.html", context)


def flight(request, flight_id):
    try:
        flight = Flight.objects.get(pk=flight_id)
    except:
        raise Http404("Flight does not exist.")
    context = {
        "flight":flight
    }

    return render(request, "flights/flight.html", context)
