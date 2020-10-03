from django.db import models

# Create your models here.

class WelcomePostModel(models.Model):

	title = models.CharField(max_length=100)

	description = models.TextField()

	image_welcome = models.ImageField(upload_to="core/uploads")

	# created and updated
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:

		verbose_name = 'Post de Bienvenida'

	def __str__(self):

		return self.title