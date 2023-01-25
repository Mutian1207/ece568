from django.contrib import admin

# Register your models here.
from .models import Users

admin.site.register(Users)
admin.site.register(Riders)
admin.site.register(Sharers)
