from django.db import models

# Create your models here.
class Items(models.Model):
	name = models.CharField(max_length=60)
	storage_details =  models.CharField(max_length=60)
	screen_size = models.CharField(max_length=60)
	camera_details =  models.CharField(max_length=60)
	battery_details =  models.CharField(max_length=60)
	processor = models.CharField(max_length=60)
	price = models.CharField(max_length=60)

	def __str__(self):
		return self.name