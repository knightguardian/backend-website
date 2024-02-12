from django.db import models

class DbModel(models.Model):
	name=models.CharField(max_length=25)
	email=models.TextField()
	password=models.TextField()
	def __str__(self):
		return self.name
