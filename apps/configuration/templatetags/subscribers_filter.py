from django.template import Library

register = Library()

def multiplicar(id):
    return str(id * 2)

register.filter("multiplicar", multiplicar)
