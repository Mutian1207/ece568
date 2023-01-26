from django.db import models

# Create your models here.
class Users(models.Model):
    VEHICLE_TYPE = (
        ('su','suv'),
        ('mp','mpv'),
        ('sd','sedan'),
        )
    user_id = models.EmailField(primary_key=True)
    user_pwd = models.CharField(max_length=30)
    is_driver = models.BooleanField(null=True, default=False)
    vehic_type = models.CharField(max_length=2, null=True, choices=VEHICLE_TYPE)
    lice_plate_number = models.CharField(max_length=10, null=True)
    max_pass_num = models.PositiveSmallIntegerField(null=True)
    other_reg = models.TextField(max_length=300, null=True)

class Rides(models.Model):
    STATUS = (
        ('op','open'),
        ('cf','confirmed'),
        ('cp','complete'),
        )
    ride_id = models.BigAutoField(primary_key=True)
    owner = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='owners')
    dest_addr = models.CharField(max_length=200)
    arr_date_time = models.DateTimeField()
    party_num = models.PositiveSmallIntegerField()
    sharable = models.BooleanField()
    status = models.CharField(max_length=2, choices=STATUS)
    driver_acc = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='drivers')
    other_reg = models.TextField(max_length=300, null=True)

class Sharers(models.Model):
    share_id = models.ForeignKey('Rides', on_delete=models.CASCADE, related_name='share_ride')
    sharer_id = models.ForeignKey('Users', on_delete=models.CASCADE, related_name='sharers')
    share_party_num = models.PositiveSmallIntegerField()
