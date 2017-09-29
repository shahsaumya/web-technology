from django.contrib import admin


# Register your models here.
from app.models import UserProfile, Movies


admin.site.register(UserProfile)
admin.site.register(Movies)