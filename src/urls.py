from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.events, name='events'),
	url(r'^(?P<event_id>\d+)/$',views.event_detail, name='event_detail')
]