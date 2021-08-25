from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.

class Post(models.Model):
	titulli = models.CharField(max_length=50, null= True, blank = True,verbose_name="Title")
	pershkrimi = models.TextField(max_length=1000, null= True, blank = True,verbose_name="Content")
	likes = models.ManyToManyField(User, related_name = "likes", blank = True)
	koha_posti = models.DateTimeField(default=timezone.now)
	autori = models.ForeignKey(User, on_delete=models.CASCADE)
	foto = models.ImageField(null= True, blank = True, height_field="height_field",width_field="width_field",upload_to="Fotot",verbose_name="Photo")
	foto2 = models.ImageField(null= True, blank = True, height_field="height_field",width_field="width_field",upload_to="Fotot",verbose_name="Second Photo")
	height_field = models.IntegerField(default=0, null= True, blank = True)
	width_field = models.IntegerField(default=0, null= True, blank = True)
	videofile= models.FileField(upload_to='videos', null=True, blank = True,verbose_name="Video")
	# public = models.BooleanField(default=False, verbose_name="Public")	
	
	def __str__(self):
		if(self.titulli):
			return self.titulli + ", " + str(self.autori)
		else:
			return str(self.autori)


	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})

	def total_likes(self):
		return self.likes.count()

class Comment(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
	koha_comment = models.DateTimeField(default=timezone.now)
	comment_autori = models.ForeignKey(User, on_delete=models.CASCADE)
	comment = models.TextField(max_length = 200, null= True, blank = True)
	photo = models.ImageField(null= True, blank = True, height_field="height_field",width_field="width_field",upload_to="Fotot-comentet")
	height_field = models.IntegerField(default=0, null= True, blank = True)
	width_field = models.IntegerField(default=0, null= True, blank = True)
	def __str__(self):
		return 'Comment by: ' + str(self.comment_autori)

	class Meta:
		ordering = ['-koha_comment']

	def get_absolute_url(self):
		return reverse('post-detail', kwargs={'pk': self.pk})