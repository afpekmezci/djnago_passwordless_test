import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserAuthManager(BaseUserManager):
	def create_user(self, CharacterName):
		user = self.model(CharacterName=CharacterName)
		user.save(using=self._db)
		return user

	def update_user(self, email, apas_id, password):
		pass

	def create_superuser(self, CharacterName):
		user = self.create_user(
			CharacterName=CharacterName,
		)
		user.is_active = True
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return User


class User(AbstractBaseUser, PermissionsMixin):
	objects = UserAuthManager()

	CharacterName = models.CharField(max_length=150, default="None", unique=True)
	AllianceID = models.BigIntegerField(null=True, blank=True)
	CorporationID = models.BigIntegerField(null=True, blank=True)
	Description = models.TextField(max_length=3000, blank=True, null=True)
	SecurityStatus = models.FloatField(blank=True, null=True)
	AccessToken = models.CharField(max_length=500, blank=True, null=True)
	TokenType = models.CharField(max_length=25, blank=True, null=True)
	ExpiresIn = models.IntegerField(blank=True, null=True)
	RefreshToken = models.CharField(max_length=150, blank=True, null=True)
	Avatar = models.CharField(max_length=150)

	start_date = models.DateTimeField(auto_now=True)
	last_login = models.DateTimeField(blank=True, null=True)

	password = None

	is_superuser = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)
	is_active = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	# password = None
	USERNAME_FIELD = 'CharacterName'

	class Meta:
		verbose_name_plural = "#Users"

	@property
	def is_authenticated(self):
		return True

	def __str__(self):
		return self.CharacterName