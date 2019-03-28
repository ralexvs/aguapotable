from django.db import models
from django.utils import timezone

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
   measurer = models.ForeignKey("Measurer",on_delete=models.CASCADE)

   
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

class TypesService(models.Model):
   detail = models.CharField(verbose_name="detalle", max_length=50)
   base_rate = models.DecimalField(verbose_name="Tarifa base", max_digits=4, decimal_places=2, default=0)
   limit = models.IntegerField(verbose_name="Rango Superior", default=11)
   excess_rate_base = models.DecimalField(verbose_name="Tarifa base excedente", max_digits=4, decimal_places=2, default=0)
   state_maximum_consumption = models.NullBooleanField(verbose_name = "Tiene limite de consumo máximo", null=True)
   maximum_consumption = models.IntegerField(verbose_name="Consumo máximo", default=0)
   maximum_consumption_value = models.DecimalField(verbose_name="Valor por consumo máximo", max_digits=5, decimal_places=2, default=0)
   created = models.DateTimeField(verbose_name="Fecha creación", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última modificación", auto_now=True)

   class Meta:
      verbose_name = ("Tipo de servicio")
      verbose_name_plural = ("Tipo de servicios")
      ordering = ['detail']

   def __str__(self):
      return self.detail

class Rate(models.Model):
   detail = models.CharField(verbose_name="Detalle", max_length=50)
   lowre_range = models.IntegerField(verbose_name="Rango Inicial", default=0)
   top_range = models.IntegerField(verbose_name="Rango Superior", default=0)
   excess_rate = models.DecimalField(verbose_name="Valor por excedente", max_digits=4, decimal_places=2, default=0)
   types_service = models.ForeignKey("TypesService", verbose_name = "Tipo de servicio", on_delete=models.CASCADE)
   created = models.DateTimeField(verbose_name="Fecha creación", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última modificación", auto_now=True)

   class Meta:
      verbose_name = ("Tabla de tarifa")
      verbose_name_plural = ("Tabla de Tarifas")
      ordering = ['detail']

   def __str__(self):
      return self.detail

class Fines(models.Model):
   detail = models.CharField(verbose_name="Detalle de la multa o sanción", max_length=50)
   sanction = models.DecimalField(verbose_name="Valor Económico", max_digits=6, decimal_places=2)
   state = models.NullBooleanField(verbose_name = "Activo", null = True)
   created = models.DateTimeField(verbose_name="Fecha creación", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última modificación", auto_now=True)
    
   class Meta:
      verbose_name = "Multa y Sanción"
      verbose_name_plural = "Multas y Sanciones"
      ordering = ['id']

   def __str__(self):
      return self.detail

class Discount(models.Model):
   detail = models.CharField(verbose_name="Tipo de Descuento", max_length=50)
   discount = models.DecimalField(verbose_name="Valor", max_digits=5, decimal_places=2)
   state = models.NullBooleanField(verbose_name = "Activo", null = True)
   created = models.DateTimeField(verbose_name="Fecha creación", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última modificación", auto_now=True)

   class Meta:
      verbose_name = "Descuento"
      verbose_name_plural = "Descuentos"
      ordering = ['id']

   def __str__(self):
      return self.detail


"""
class ServiceRequest(models.Model):
   request_date = models.DateTimeField(verbose_name="Fecha de Solicitud", default = timezone.now())
   subscribers = models.ForeignKey("Subscribers", verbose_name= "Abonado", on_delete=models.CASCADE)
   rate = models.ForeignKey("Rate", verbose_name="Servicio", on_delete=models.CASCADE)



   class Meta:
      verbose_name = _("Solicitud de servicio")
      verbose_name_plural = _("Solicitud de servicio")
      ordering = ['id']

   def __str__(self):
      return self.name

""" 


# DATOS PARA SRI

#Tabla 4
''' El código que conformará el tipo de ambiente según la clave de acceso se cita a continuación:'''
TESTS = 1
PRODUCTION = 2
TYPE_OF_ENVIRONMENT = (
   (TESTS, 'PRUEBAS'),
   (PRODUCTION, 'PRODUCCION'),
   )

class Company(models.Model):
   ruc = models.CharField(verbose_name="Ruc", max_length=13)
   business_name = models.CharField(max_length=100, unique=True, verbose_name="Apellidos y Nombres: Razón Social")
   tradename = models.CharField(verbose_name="nombre comercial", max_length=60, blank=True)
   main_address = models.TextField(verbose_name="Dirección Matriz", max_length=200)
   special_contributor = models.CharField(verbose_name="contribuyente Especial", max_length=10, blank=True)
   forced_to_keep_accounting = models.BooleanField(verbose_name="obligado a llevar contabilidad", default=False)
   logo = models.ImageField(verbose_name="Logotipo", upload_to='configuration/logo/',null=True,blank=True)
   type_of_enviroment = models.IntegerField(choices=TYPE_OF_ENVIRONMENT, default=TESTS)
   ANF_1 = 1
   ANF_2 = 2
   BCE_1 = 3
   BCE_2 = 4
   SD_1 = 5
   SD_2 = 6
   KEY_4 = 7
   TOKEN = (
      (ANF_1,'ANF - Certificado Exportado'),
      (ANF_2,'ANF - Plug & Sing'),
      (BCE_1,'BCE - ikey2032'),
      (BCE_2,'BCE - Aladin eToken Pro'),
      (SD_1,'SD - ePass3030 auto'),
      (SD_2,'SD - BioPass3000'),
      (KEY_4,'Key4 - Consejo Judicatura'),
   )
   token_to_sign = models.IntegerField(verbose_name="Token para firmar", choices=TOKEN,default=BCE_1)
   phone = models.CharField(verbose_name="Teléfono", max_length=10)
   mobile = models.CharField(verbose_name="Celular", max_length=10)
   email = models.EmailField(verbose_name="Email", max_length=60)
   web = models.URLField(verbose_name="Página web", max_length=60, blank=True)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.business_name + " " + self.tradename

   class Meta:
      verbose_name = 'Entidad'   
      verbose_name_plural = 'Entidad Emisor'



#Tabla 1
''' Cada comprobante generado contendrá una clave de acceso única que estará compuesta por 49
dígitos numéricos, el aplicativo a utilizar por el sujeto pasivo deberá generar de manera automática
esta clave, la cual constituye un requisito obligatorio que le dará el carácter de único a cada
comprobante y a la vez se constituirá en el número de autorización del mismo; en base a esta clave
el SRI generará la respuesta de autorizado o no; a continuación se describe su conformación: '''

class KeyConformation(models.Model):
   date_of_issue = models.DateField(verbose_name="Fecha de Emisión", max_length=8)
   type_voucher = models.ForeignKey('TypeVoucher', verbose_name="tipo de comprobante" ,on_delete=models.CASCADE)
   ruc = models.ForeignKey('Company', verbose_name="Ruc",  on_delete=models.CASCADE)
   TYPE_OF_ENVIRONMENT = models.IntegerField(verbose_name="Tipo de Ambiente", choices=TYPE_OF_ENVIRONMENT, default=TESTS)
   series = models.CharField(verbose_name="Serie", max_length=6)
   voucher_number= models.CharField(verbose_name="Número de comprobante", max_length=9)
   numeric_code = models.BigIntegerField(verbose_name="Código Numérico" )
   type_of_emission = models.ForeignKey('Emission',verbose_name="tipo de Emisión", on_delete=models.CASCADE)
   check_digit = models.IntegerField()
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.series + self.voucher_number
   class Meta:
      verbose_name = 'Conformación clave'
      verbose_name_plural='Conformación clave'

#Tabla 2
''' El código que conformará el tipo de emisión según la clave de acceso generada se detalla a
continuación: '''


class Emission(models.Model):
   rcode = models.CharField(verbose_name="Código", max_length=2)
   detail = models.CharField(verbose_name="Detalle", max_length=60)
   ceated = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.detail

#Tabla 3
''' Los tipos de comprobantes que pueden generar los contribuyentes de manera electrónica se detalla
conforme al siguiente cuadro: '''

class TypeVoucher(models.Model):
   code = models.CharField(verbose_name="Código", max_length=2)
   detail = models.CharField(verbose_name="detalle", max_length=60)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.detail



# Tabla 5
''' Los contribuyentes que generen sus comprobantes de venta, retención y documentos
complementarios firmados electrónicamente en el ambiente de pruebas, pueden hacer constar en
el campo de la Razón Social del receptor, destinatario y agente retenido la denominación
PRUEBAS SERVICIO DE RENTAS INTERNAS. '''

class Tests(models.Model):
   identification = models.ForeignKey('Identification', verbose_name='Identificación', on_delete=models.CASCADE, null=False)
   number = models.CharField(verbose_name='Número', max_length=13)
   business_name = models.CharField(verbose_name='Razón social', max_length=100)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.number + " " + self.business_name



#Tabla 6 (Identificacion del Documento)
''' Conforme al tipo de transacción efectuada deberá señalar el tipo de cliente, sujeto retenido o
destinatario, según el detalle: '''

class Identification(models.Model):
   code = models.CharField(verbose_name='Código', max_length=2)
   detail = models.CharField(verbose_name='Detalle', max_length=60)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.detail

#Tabla 7
''' Es responsabilidad y obligación del sujeto pasivo enviar el comprobante electrónico al SRI de
manera individual o en lote; así también deberá confirmar que el comprobante haya sido
autorizado. A continuación se describen los estados del comprobante electrónico. '''

class State(models.Model):
   electronic_voucher_status = models.CharField(verbose_name='Estado del comprobante electróncio', max_length=60)
   acronym = models.CharField(verbose_name='siglas', max_length=3)
   created = models.DateTimeField(verbose_name="Fecha admisión", auto_now_add=True)
   modified = models.DateTimeField(verbose_name="Última Modificación", auto_now=True)

   def __str__(self):
      return self.electronic_voucher_status

