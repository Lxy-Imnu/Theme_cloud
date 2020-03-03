from django.contrib import admin

# Register your models here.
from . import models
class user_admin(admin.ModelAdmin):
    list_display = ('id','name')
    list_per_page = 3
    search_fields = ('id','name')
admin.site.register(models.User,user_admin)