from django.shortcuts import render

# Create your views here.

from .models import Question
from .forms import QuestionForm

def questions(request):
	questions = Question.objects.all()
	context = {
		'questions': questions
	}
	return render(request, 'questions/questions.html', context)

def ask(request):
	form = QuestionForm()
	context = {
		"form": form
	}
	return render(request, 'questions/ask.html', context)	

