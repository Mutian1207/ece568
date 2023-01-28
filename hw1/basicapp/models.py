from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Users require an email field')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class Users(AbstractUser):
    VEHICLE_TYPE = (
        ('su','suv'),
        ('mp','mpv'),
        ('sd','sedan'),
        )
    username = None
    email = models.EmailField(unique = True)
    #user_pwd = models.CharField(max_length=30)
    is_driver = models.BooleanField(null=True, default=False)
    vehic_type = models.CharField(max_length=2, null=True, choices=VEHICLE_TYPE)
    lice_plate_number = models.CharField(max_length=10, null=True)
    max_pass_num = models.PositiveSmallIntegerField(null=True)
    other_reg = models.TextField(max_length=300, null=True)
    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
class Rides(models.Model):
    STATUS = (
        ('op','open'),
        ('cf','confirmed'),
        ('cp','complete'),
        )
    ride_id = models.BigAutoField(primary_key=True,auto_created=True)
    owner = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='owners',null=True)
    dest_addr = models.CharField(max_length=200)
    arr_date_time = models.DateTimeField()
    party_num = models.PositiveSmallIntegerField()
    sharable = models.BooleanField(null=True)
    status = models.CharField(max_length=2, choices=STATUS,null=True)
    driver_acc = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='drivers',null=True)
    other_reg = models.TextField(max_length=300, null=True)
    
class Sharers(models.Model):
    share_id = models.ForeignKey('Rides', on_delete=models.CASCADE, related_name='share_ride')
    sharer_id = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='sharers')
    share_party_num = models.PositiveSmallIntegerField()
