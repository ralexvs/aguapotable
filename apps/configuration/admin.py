from django.contrib import admin
from .models import (
    Subscribers, 
    Measurer, 
    Brand, 
    Company, 
    TypesService, 
    Rate,
    Fines,
)

# Register your models here.
admin.site.register(Subscribers)
admin.site.register(Measurer)
admin.site.register(Brand)
admin.site.register(Company)
admin.site.register(TypesService)
admin.site.register(Rate)
admin.site.register(Fines)

"""
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'business_name','tradename')
    search_fields = ('ruc', 'business_name','tradename')    





class TypeVoucherAdmin(admin.ModelAdmin):
    list_display = ('detail','code')
    search_fields = ('detail','code')
    ordering = ('detail','code')

class TestsAdmin(admin.ModelAdmin):
    list_display = ('number','identification','business_name')
    search_fields = ('number','identification','business_name')
    ordering = ('number','identification','business_name')

class IdentificationAdmin(admin.ModelAdmin):
    list_display = ('code','detail')
    search_fields = ('code','detail')
    ordering = ('code','detail')
    """