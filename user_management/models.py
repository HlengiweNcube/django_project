from django.conf import settings
from django.db import models


class UserProfile(models.Model):
	"""Stores additional contact details required by the assignment."""

	user = models.OneToOneField(
		settings.AUTH_USER_MODEL,
		on_delete=models.CASCADE,
		related_name='profile'
	)
	phone_number = models.CharField(max_length=30, blank=True)
	address = models.CharField(max_length=255, blank=True)
	city = models.CharField(max_length=120, blank=True)
	country = models.CharField(max_length=120, blank=True)
	postal_code = models.CharField(max_length=20, blank=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return f"Profile for {self.user.username}"
