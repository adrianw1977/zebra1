from django.db import models
from ..users.models import User


class ArtWorx(models.Model):
	artname = models.TextField(max_length=255)
	description = models.TextField(max_length=1000)
	creator = models.ForeignKey(User, related_name="creator")
	# travellers = models.ManyToManyField(User, related_name="travellers")
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	totalpnts = models.IntegerField(default=100)
	totalpntstyle = models.IntegerField(default=100)
	totalpntsorig = models.IntegerField(default=100)
	totalpntstech = models.IntegerField(default=100)
