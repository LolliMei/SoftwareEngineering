from django.contrib import admin

# Register your models here.
from .models import user_profile_stu, imageprofile, ConfirmString, user_profile_teh

admin.site.register(user_profile_stu)
admin.site.register(imageprofile)
admin.site.register(ConfirmString)
admin.site.register(user_profile_teh)
