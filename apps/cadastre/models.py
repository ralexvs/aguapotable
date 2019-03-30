from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField
from apps.configuration.models import Rate, PaymentMethods, Discount


# Create your models here.


class Subscribers(models.Model):

   identification = models.CharField(verbose_name="Cédula / Ruc", max_length=13, unique=True)  
   surname = models.CharField(verbose_name="Apellido", max_length=60)
   name = models.CharField(verbose_name="Nombre", max_length=60)
   address = models.CharField(verbose_name="Dirección", max_length=254)
   email = models.EmailField(verbose_name="Correo", max_length=100, unique=True)
   phone = models.CharField(verbose_name="Teléfono", max_length=15)
   mobile = models.CharField(verbose_name="Celular", max_length=15, blank=True, null=True)
   state = models.NullBooleanField(verbose_name="estado", null=True)
   birth_date = models.DateField(verbose_name='Fecha de Nacimieno',null=True,blank=True)
   portrait = models.ImageField(verbose_name='Retrato', upload_to='configuration/subscribers/', height_field=None, width_field=None, max_length=None, blank=True, null=True) 
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   
   class Meta:
      verbose_name = "Abonado"
      verbose_name_plural = "Abonados"
      ordering = ["surname"]

   def __str__(self):
      return self.identification + self.surname + self.name


class Measurer(models.Model):

   """Model defn for Measurer."""

   number = models.CharField(verbose_name="Número", max_length=50, unique=True)
   detail = models.CharField(verbose_name="Detalle", max_length=254)
   brand = models.ForeignKey("Brand", verbose_name="Marca", on_delete=models.CASCADE)
   model = models.CharField(verbose_name="Modelo", max_length=30)
   initial_reading = models.IntegerField(verbose_name="Lectura inicial")
   state = models.NullBooleanField(verbose_name="Estado", null=True)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)


   # TODO: Define fields here
   
   def get_context_data(self,*args, **kwargs):
      context = super(Measurer, self).get_context_data(*args, **kwargs)
      context = "Hsola Contexto"
      return context
   
   class Meta:
      """Meta defn for Measurer."""

      verbose_name = 'Medidor'
      verbose_name_plural = 'Medidores'
      ordering = ["id"]

   def __str__(self):
      """Unicode represon of Measurer."""
      return self.detail
   

class Brand(models.Model):
   detail = models.CharField(verbose_name="Detalle", max_length=50)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)
   
   class Meta:
      """Meta defn for Brand."""

      verbose_name = 'Marca'
      verbose_name_plural = 'Marcas'
      ordering = ["detail"]

   def __str__(self):
      """Unicode represon of Brand."""
      return self.detail


"""
class Cadastral(models.Model):
   cadastre_number = models.IntegerField(verbose_name="Numero catastral", unique=True)
   date_admission = models.DateTimeField(verbose_name="Fecha de Ingreso")
   subscribers = models.ForeignKey("Subscribers", verbose_name= "Abonado", on_delete=models.CASCADE)
   rate = models.ForeignKey("Rate", verbose_name="Servicio", on_delete=models.CASCADE)
   payment_methods = models.ForeignKey("PaymentMethods", verbose_name="Forma de Pago", on_delete=models.CASCADE)
   measurer = models.ForeignKey("Measurer", verbose_name="Medidor", on_delete=models.CASCADE)
   discount = models.ForeignKey("Discount", verbose_name="Tipo descuento", on_delete=models.CASCADE)
   detail = RichTextField(verbose_name="Detalle", blank=True, null=True)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)


   class Meta:
      verbose_name = "Planilla catastral"
      verbose_name_plural = "Planillas Catastrales"
      ordering = ['id']

   def __str__(self):
      return self.name

 
"""
