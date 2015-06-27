from django.shortcuts import render
import datetime


# Create your views here.
from src.models import Event

def events(request):
	now = datetime.datetime.now()
	tmrw = datetime.date.today() + datetime.timedelta(days = 1)
	tmrw_day = str(tmrw.strftime("%d"))

	events_today = Event.objects.filter(event_date__day = now.strftime("%d"))
	events_tmrw = Event.objects.filter(event_date__day = now.strftime("%d"))
	events_all = Event.objects.all()
	return render(request, 'events.html',{'events_all' : events_all, 'events_today' : events_today})


def event_detail(request, event_id):
	detail_event = Event.objects.get(pk=event_id)
	return render(request,'event_detail.html',{'detail_event':detail_event})


