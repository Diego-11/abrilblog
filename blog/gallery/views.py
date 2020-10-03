from django.shortcuts import render
from .models import PostModel

# Create your views here.


def gallery(request):

	context = {
		'title': 'Publicaciones',
		'posts': PostModel.objects.all()
	}

	return render(request, 'gallery/posts.html', context)