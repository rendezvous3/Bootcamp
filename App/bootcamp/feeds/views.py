from django.shortcuts import render

# Create your views here.

from feeds.models import Feed

def home(request):
	feeds = Feed.objects.all()
	context = {
		'feeds': feeds,
	}
	return render(request, 'feeds/feeds.html', context)