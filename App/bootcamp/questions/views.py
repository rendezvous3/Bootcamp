from django.shortcuts import render

# Create your views here.

from .models import Question

def questions(request):
	questions = Question.objects.all()
	context = {
		'questions': questions
	}
	return render(request, 'questions/questions.html', context)

