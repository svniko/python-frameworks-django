from django.shortcuts import render
from django.http import HttpResponse
from . models import Flight, Airport
from . forms import FlightForm

# Create your views here.
def index(request):
    return render(request, "flights/index.html",{
        'flights': Flight.objects.all()
    })

def flight(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    passengers = flight.passengers.all()
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": passengers
    })

def forms_page(request):
   
    # create object of form
    form = FlightForm(request.POST)
      # check if form data is valid
    if form.is_valid():

        # save the form data to model
        form.save()
    form = FlightForm()
    return render(request, "flights/forms.html", {
        	   'form':form,
            })
