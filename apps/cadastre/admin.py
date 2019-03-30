from django.contrib import admin
from .models import Subscribers, Measurer, Brand

# Register your models here.

admin.site.register(Subscribers)
admin.site.register(Brand)
admin.site.register(Measurer)

