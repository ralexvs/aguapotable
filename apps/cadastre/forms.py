from django.forms import ModelForm
from .models import (
    Subscribers, 
    Measurer, 
    Cadastral,
     )

class SubscribersForm(ModelForm):
    
    class Meta:
        model = Subscribers
        fields = ['identification','surname','name','address','email','phone','mobile','state','birth_date']

    def __init__(self, *args, **kwargs):
            super(SubscribersForm, self).__init__(*args, **kwargs)
            for field in iter(self.fields):
                if field != 'state':
                    self.fields[field].widget.attrs.update({
                        'class': 'form-control'
                    })

class MeasurerForm(ModelForm):
    
    class Meta:
        model = Measurer
        fields = ('number','detail','brand','model','initial_reading','state')
    
    def __init__(self, *args, **kwargs):
        super(MeasurerForm,self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            if field != 'state':
                self.fields[field].widget.attrs.update({'class':'form-control'})

class CadastralForm(ModelForm):
    
    class Meta:
        model = Cadastral
        fields = ('cadastre_number','date_admission','subscribers','rate','payment_methods','measurer','discount','detail','state')
        
    def __init__(self, *args, **kwargs):
        super(CadastralForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'state':
                self.fields[field].widget.attrs.update({'class':'form-control'})

