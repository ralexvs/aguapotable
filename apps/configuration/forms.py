from django.forms import ModelForm
from .models import (
    Subscribers, 
    Measurer, 
    Company, 
    TypesService, 
    Rate,
    Fines,
    Discount,
    )

class SubscribersForm(ModelForm):
    
    class Meta:
        model = Subscribers
        fields = ['identification','surname','name','address','email','phone','mobile','state','birth_date','measurer']

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


class CompanyForm(ModelForm):
    
    class Meta:
        model = Company
        fields = ('ruc','business_name','tradename','main_address','special_contributor','forced_to_keep_accounting','logo','type_of_enviroment','token_to_sign','phone','mobile','email','web')
    
    def __init__(self, *args, **kwargs):
        super(CompanyForm,self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})

class TypesServiceForm(ModelForm):
    
    class Meta:
        model = TypesService
        fields = ('detail','base_rate','limit','excess_rate_base','state_maximum_consumption','maximum_consumption','maximum_consumption_value')
        
    def __init__(self, *args, **kwargs):
        super(TypesServiceForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            if field != 'state_maximum_consumption':
                self.fields[field].widget.attrs.update({'class':'form-control'})

class RateForm(ModelForm):
    
    class Meta:
        model = Rate
        fields = ('detail','lowre_range','top_range','excess_rate','types_service')

    def __init__(self, *args, **kwargs):
        super(RateForm,self).__init__(*args, **kwargs)

        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({'class':'form-control'})
            

class FinesForm(ModelForm):
    
    class Meta:
        model = Fines
        fields = ('detail','sanction','state')
    
    def __init__(self, *args, **kwargs):
        super(FinesForm, self).__init__(*args, **kwargs)

        for field in iter(self.fields):

            if field != 'state':
                self.fields[field].widget.attrs.update({'class':'form-control'})

class DiscountForm(ModelForm):
    
    class Meta:
        model = Discount
        fields = ('detail','discount','state')

    def __init__(self, *args, **kwargs):
        super(DiscountForm, self).__init__(*args, **kwargs)
        
        for field in iter(self.fields):
            if field != 'state':
                self.fields[field].widget.attrs.update({'class': 'form-control'})



        

    
    



