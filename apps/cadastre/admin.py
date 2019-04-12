from django.contrib import admin
from .models import Subscribers, Measurer, Brand, Readings, ReadingsDetail, Cadastral


class CadastralAdmin(admin.ModelAdmin):
   list_display = ['cadastre_number','date_admission','subscribers','rate','payment_methods']
   list_filter = ['rate','payment_methods']
   search_fields = ['cadastre_number','date_admission','subscribers','rate','payment_methods']
   
   class Media:
      css = {
         'all': ('core/css/custom_ckeditor.css',)
      }
    

# Register your models here.

admin.site.register(Subscribers)
admin.site.register(Brand)
admin.site.register(Measurer)
admin.site.register(Readings)
admin.site.register(ReadingsDetail)
admin.site.register(Cadastral, CadastralAdmin)
