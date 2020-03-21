from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class MyAccountManager(BaseUserManager):
	def create_user(self, email, username, password=None):
		if not email:
			raise ValueError("Users must have an email adress")
		if not username:
			raise ValueError("Users must have a username")

		user = self.model(
				email=self.normalize_email(email)
				username=username,
			)

		user.set_password(password)
		user.save(self._db)
		return user

	def create_superuser(self, email, username, password):
			user = self.model(
				email=self.normalize_email(email)
				password=password,
				username=username,
			)
			user.is_admin=True
			user.is_staff=True
			user.is_superuser=True
			user.save(using=self._db)

class Account(AbstractBaseUser):
	email					= models.EmailField(verbose_name="email", max_length=60,unique=True)
	username				= models.CharField(max_length=30, unique=True)
	date_joined				= models.DateTimeField(verbose_name="date joined", auto_now_add=True)
	last_login				= models.DateTimeField(verbose_name="last login", auto_now=True)
	is_admin				= models.BooleanFiled(default=False)
	is_active				= models.BooleanFiled(default=True)
	is_staff				= models.BooleanFiled(default=False)
	is_superuser			= models.BooleanFiled(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return self.is_admin

	def has_module_permissios(self, app_label):
		return True
