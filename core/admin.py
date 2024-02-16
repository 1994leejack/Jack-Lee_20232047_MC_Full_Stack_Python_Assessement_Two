from django.contrib import admin
from .models import RenewablePowerGeneration, Article, Subscriber

# Register your models here.

admin.site.register(RenewablePowerGeneration)
admin.site.register(Article)
admin.site.register(Subscriber)