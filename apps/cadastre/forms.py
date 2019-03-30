from django.forms import ModelForm
from .models import (
    Subscribers, 
    Measurer, 
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

