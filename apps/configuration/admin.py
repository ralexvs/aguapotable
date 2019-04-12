from django.contrib import admin
from .models import (
    Company, 
    TypesService, 
    Rate,
    Fines,
    PaymentMethods,
)



class RateAdmin(admin.ModelAdmin):
    list_display = ('detail', 'lowre_range','top_range')
    search_fields = ('detail', 'lowre_range','top_range')
    list_filter = ('detail', 'lowre_range','top_range')
    readonly_fields = ('created','modified')

    
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('ruc', 'business_name','tradename')
    search_fields = ('ruc', 'business_name','tradename')    
    readonly_fields = ('created','modified')

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

# Register your models here.
admin.site.register(Company, CompanyAdmin)
admin.site.register(TypesService)
admin.site.register(Rate, RateAdmin)
admin.site.register(Fines)
admin.site.register(PaymentMethods)
