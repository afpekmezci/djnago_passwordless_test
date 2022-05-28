from django.contrib import admin
from secondapp.models import SomeModel


@admin.register(SomeModel)
class SomeModelAdmin(admin.ModelAdmin):
	pass