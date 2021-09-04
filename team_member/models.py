from django.db import models
from phone_field import PhoneField

role_choices = ((False, "Regular - Can't delete team members"),
                (True, "Admin - Can delete team members"))

# Create your models here.
class TeamMember(models.Model):
    picture = models.ImageField(upload_to='profile_pictures', blank=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = PhoneField(blank=True)
    admin_role = models.BooleanField(default=False, choices=role_choices)
