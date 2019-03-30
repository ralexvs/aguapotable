from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from .models import (
    Company, 
    TypesService, 
    Rate, 
    Fines,
    Discount,
    PaymentMethods,
    )

from .forms import (
    CompanyForm, 
    TypesServiceForm,
    RateForm,
    FinesForm,
    DiscountForm,
    PaymentMethodsForm,
    )


# Create your views here.

#ListView
    
class CompanyListView(ListView):
    model = Company

class TypesServiceListView(ListView):
    model = TypesService

class RateListView(ListView):
    model = Rate

class FinesListView(ListView):
    model = Fines

class DiscountListView(ListView):
    model = Discount

class PaymentMethodsListView(ListView):
    model = PaymentMethods



#DetailView

class CompanyDetailView(DetailView):
    model = Company

class TypesServiceDetailView(DetailView):
    model = TypesService

class RateDetailView(DetailView):
    model = Rate

class FinesDetailView(DetailView):
    model = Fines


class DiscountDetailView(DetailView):
    model = Discount


class PaymentMethodsDetailView(DetailView):
    model = PaymentMethods


#CreateView

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'configuration/company_form.html'
    success_url = reverse_lazy('ajustes:company_list')

class TypesServiceCreateView(CreateView):
    model = TypesService
    form_class = TypesServiceForm
    template_name = "configuration/typesservice_form.html"
    success_url = reverse_lazy('ajustes:typesservice_list')

class RateCreateView(CreateView):
    model = Rate
    form_class = RateForm
    template_name = "configuration/rate_form.html"
    success_url = reverse_lazy('ajustes:rate_list')

class FinesCreateView(CreateView):
    model = Fines
    form_class = FinesForm
    template_name = 'configuration/fines_form.html'
    success_url = reverse_lazy('ajustes:fines_list')


class DiscountCreateView(CreateView):
    model = Discount
    form_class = DiscountForm
    template_name = "configuration/discount_form.html"
    success_url = reverse_lazy('ajustes:discount_list')

class PaymentMethodsCreateView(CreateView):
    model = PaymentMethods
    form_class = PaymentMethodsForm
    template_name = "configuration/paymentmethods_form.html"
    success_url = reverse_lazy('ajustes:paymentmethods_list')




#UpdateView
    
class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('ajustes:company_update', args=[self.object.id]) + '?ok'

class TypesServiceUpdateView(UpdateView):
    model = TypesService
    form_class = TypesServiceForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ajustes:typesservice_update', args=[self.object.id]) + '?ok'

class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('ajustes:rate_update', args=[self.object.id]) + '?ok'

class FinesUpdateView(UpdateView):
    model = Fines
    form_class = FinesForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('ajustes:fines_update', args =[self.object.id]) + '?ok'


class DiscountUpdateView(UpdateView):
    model = Discount
    form_class = DiscountForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('ajustes:discount_update', args =[self.object.id]) + '?ok'

class PaymentMethodsUpdateView(UpdateView):
    model = PaymentMethods
    form_class = PaymentMethodsForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('ajustes:paymentmethods_update', args = [self.object.id]) + '?ok'



#DeleteView

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('ajustes:company_list')

class TypesServiceDeleteView(DeleteView):
    model = TypesService
    success_url = reverse_lazy('ajustes:typesservice_list')

class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('ajustes:rate_list')

class FinesDeleteView(DeleteView):
    model = Fines
    success_url = reverse_lazy('ajustes:fines_list')


class DiscountDeleteView(DeleteView):
    model = Discount
    success_url = reverse_lazy('ajustes:discount_list')

class PaymentMethodsDeleteView(DeleteView):
    model = PaymentMethods
    success_url = reverse_lazy('ajustes:paymentmethods_list')

