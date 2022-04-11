from django.contrib import admin

from profiles_api import models

admin.site.register(models.UserProfile)
admin.site.register(models.Course)
admin.site.register(models.Registration)
admin.site.register(models.FatherFamily)