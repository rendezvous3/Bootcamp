"""bootcamp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static    

from feeds.views import home, post
from questions.views import questions, ask, question, answered, unanswered, answer, accept
admin.autodiscover()

urlpatterns = [
	url(r'^$', home, name="feeds"),
    url(r'^post/$', post, name='post'),
	url(r'^questions/$', questions, name="questions"),
    url(r'^questions/(?P<pk>\d+)/$', question, name="question"),
    url(r'^questions/answered/$', answered, name="answered"),
    url(r'^questions/unanswered/$', unanswered, name="unanswered"),
    url(r'^questions/ask/$', ask, name="ask"),
    url(r'^questions/answer/$', answer, name="answer"),
    url(r'^questions/answer/accept/$', accept, name="accept"),
    url(r'^admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
