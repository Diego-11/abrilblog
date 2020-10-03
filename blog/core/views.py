from django.shortcuts import render
from .models import WelcomePostModel

# Create your views here.


def home(request):

	post = WelcomePostModel.objects.get(pk=1)

	context = {'title': 'Home',
				'post': post}

	return render(request, 'core/welcome.html', context)
