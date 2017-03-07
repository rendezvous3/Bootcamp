from django.shortcuts import render

# Create your views here.

from feeds.models import Feed

def home(request):
	feeds = Feed.objects.all()
	context = {
		'feeds': feeds,
	}
	return render(request, 'feeds/feeds.html', context)

def post(request):
    feed = Feed()
    feed.user = request.user
    # data: $("#compose-form").serialize(),
    feed.post = request.POST['post']
    feed.save()
    return render(request, 'feeds/partial_feed.html', {'feed': feed})		