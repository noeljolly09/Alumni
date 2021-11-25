from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from datetime import date

from Events.models import eventsData

# Create your views here.

@login_required
def allEvents(request):
    events = eventsData.objects.all()
    return render(request, 'events/all_events.html',{'events':events})

@login_required
def addEvents(request):
    if request.method == "POST":
        name = request.POST['name']
        eve_image = request.FILES['image']
        eve_date = request.POST['date']
        eve_time = request.POST['time']
        description = request.POST['description']
        event = eventsData.objects.create(event_name=name,event_image=eve_image,event_date=eve_date,event_time=eve_time,event_description=description,creation_date=date.today())
        event.save()
        return redirect('allevents')

    return render(request, 'events/events_add.html')

