from django.db import models
from django.contrib.auth.models import User
#from django.contrib.auth.models import AbstractUser
# Create your models here.

"""
class CustomUser(AbstractUser):
    USER_ROLES = (
        ('farmer', 'Farmer'),
        ('researcher', 'Researcher'),
    )
    user_role = models.CharField(max_length=10, choices=USER_ROLES)

    groups = models.ManyToManyField(
            'auth.Group', 
            verbose_name='groups', 
            blank=True, 
            related_name='user_set9', 
            help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.'
            )
    user_permissions = models.ManyToManyField(
    'auth.Permission',
    verbose_name='user permissions',
    blank=True,
    related_name='user_permission_set',
    help_text='Specific permissions for this user.',
    related_query_name='user',
    )
"""

class SoilData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    soil_type = models.CharField(max_length=100)
    ph_level = models.CharField(max_length=100)
    nutrient_content = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    other_fields = models.TextField()


class ChatMessage(models.Model):
    user_input = models.TextField()
    model_response = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"User: {self.user_input[:50]} | Model: {self.model_response[:50]}"

    class Meta:
        ordering = ['timestamp']

