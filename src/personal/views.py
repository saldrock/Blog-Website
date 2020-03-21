from django.shortcuts import render
from personal.models import question

def home_screen_view(request):
	context={}

	questions=question.objects.all()
	context['questions'] = questions

	return render(request, "personal/home.html", context)