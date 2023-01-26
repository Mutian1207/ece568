from django.contrib import admin

# Register your models here.
from .models import Users
from .models import Rides
from .models import Sharers

admin.site.register(Users)
admin.site.register(Rides)
admin.site.register(Sharers)
