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
	if request.method == "POST":
		form = QuestionForm(request.POST)
		if form.is_valid():
			question = Question()
			question.user = request.user
			question.title = form.cleaned_data.get('title')
			question.description = form.cleaned_data.get('description')
			question.tags = form.cleaned_data.get('tags')
			question.save()
			return redirect('questions')
		else:
			return render(request, 'questions/ask.html', {'form': form})
	else:
		form = QuestionForm()			
		context = {
			"form": form
		}
	return render(request, 'questions/ask.html', context)	

