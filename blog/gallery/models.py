from django.db import models

# Create your models here.

class PostModel(models.Model):

	id = models.AutoField(primary_key=True)

	title = models.CharField(max_length=100)

	description = models.TextField()

	image = models.ImageField(upload_to="core/uploads")

	# created and updated
	created = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	class Meta:

		verbose_name = 'Publicación del Blog'
		verbose_name_plural = 'Publicaciones del Blog'

	def __str__(self):

		return self.title