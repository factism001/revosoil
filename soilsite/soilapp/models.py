from django.db import models
from django.contrib.auth.models import AbstractUser
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
    #user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    soil_type = models.CharField(max_length=100)
    ph_level = models.DecimalField(max_digits=4, decimal_places=2)
    nutrient_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    #user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    other_fields = models.TextField()
