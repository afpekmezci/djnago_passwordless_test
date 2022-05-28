from django.db import models


class SomeModel(models.Model):
	some_field = models.CharField(max_length=2)
