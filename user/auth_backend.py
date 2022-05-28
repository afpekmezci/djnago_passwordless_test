from django.contrib.auth.backends import BaseBackend
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()


class CustomLoginBackend(ModelBackend):

	def authenticate(self, request, username=None, **kwargs):
		print('my login backend')
		if username is None:
			username = kwargs.get(UserModel.USERNAME_FIELD)
		if username is None:
			return
		try:
			user = UserModel._default_manager.get_by_natural_key(username)
		except UserModel.DoesNotExist:
			# Run the default password hasher once to reduce the timing
			# difference between an existing and a nonexistent user (#20760).
			return
		else:
			if self.user_can_authenticate(user):
				return user
