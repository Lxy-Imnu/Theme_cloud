from django.contrib import admin
from app.models import User
from app.models import Spider
from app.models import Message

# Register your models here.

admin.site.register(User)
admin.site.register(Spider)
admin.site.register(Message)


