from django.shortcuts import render, redirect

# Create your views here.

from .models import Question
from .forms import QuestionForm

def questions(request):
	questions = Question.objects.all()
	context = {
		'questions': questions,
		'active': 'all'
	}
	return render(request, 'questions/questions.html', context)

def answered(request):
	questions = Question.get_answered()
	context = {
		'questions': questions,
		'active': 'answered'
	}
	return render(request, 'questions/questions.html', context)

def unanswered(request):
	questions = Question.get_unanswered()
	context = {
		'questions': questions,
		'active': 'unanswered'
	}
	return render(request, 'questions/questions.html', context)			

def ask(request):
	form = QuestionForm()
	context = {
		"form": form
	}
	return render(request, 'questions/ask.html', context)	

