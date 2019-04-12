from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


# Create your models here.

def custom_upload_to(instance,filename):
   old_instance=Profile.objects.get(pk=instance.pk)
   old_instance.avatar.delete()
   return 'registration/profile/' + filename


class Profile(models.Model):
   user = models.OneToOneField(User, verbose_name='Usuario', on_delete=models.CASCADE)
   avatar = models.ImageField(verbose_name='Avatar', upload_to=custom_upload_to, height_field=None, width_field=None, max_length=None, blank=True, null=True) 
   bio = RichTextField(verbose_name='Biografía', null = True, blank=True)
   link = models.URLField(verbose_name='Enlace', max_length=200, null=True, blank=True)

   class Meta:
      ordering = ['user__username']

@receiver(post_save,sender=User)
def ensure_profile_exists(sender, instance,**kwargs):
    if kwargs.get('created',False):
        Profile.objects.get_or_create(user=instance)
        print('Se acaba de crear un usuario y su perfil enlazado')
