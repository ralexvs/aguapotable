from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy
from .models import (
    Subscribers, 
    Company, 
    TypesService, 
    Measurer,
    Rate, 
    Fines,
    Discount,
    )

from .forms import (
    SubscribersForm, 
    MeasurerForm, 
    CompanyForm, 
    TypesServiceForm,
    RateForm,
    FinesForm,
    DiscountForm,
    )


# Create your views here.

#ListView
class SubscribersListView(ListView):
    model = Subscribers
    #template_name = "configuration/list_subscribers.html"
    paginate_by = 10
    
class CompanyListView(ListView):
    model = Company

class MeasurerListView(ListView):
    model = Measurer
    paginate_by = 10

class TypesServiceListView(ListView):
    model = TypesService

class RateListView(ListView):
    model = Rate


class FinesListView(ListView):
    model = Fines


class DiscountListView(ListView):
    model = Discount



#DetailView

class SubscribersDetailView(DetailView):
    model = Subscribers

class MeasurerDetailView(DetailView):
    model = Measurer

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


#CreateView

class SubscribersCreateView(CreateView):
    model = Subscribers
    form_class = SubscribersForm
    template_name = "configuration/subscribers_form.html"
    success_url = reverse_lazy('ajustes:subscribers_list')

class MeasurerCreateView(CreateView):
    model = Measurer
    form_class = MeasurerForm
    template_name = "configuration/measurer_form.html"
    success_url = reverse_lazy('ajustes:measurer_list')

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




#UpdateView
    
class SubscribersUpdateView(UpdateView):
    model = Subscribers
    form_class = SubscribersForm
    template_name_suffix  = "_update_form"
    
    def get_success_url(self):
        return reverse_lazy('ajustes:subscribers_update', args=[self.object.id]) + '?ok'

class MeasurerUpdateView(UpdateView):
    model = Measurer
    form_class = MeasurerForm
    template_name_suffix = "_update_form"

    def get_success_url(self):
        return reverse_lazy('ajustes:measurer_update', args=[self.object.id]) + '?ok'

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



#DeleteView

class SubscribersDeleteView(DeleteView):
    model = Subscribers
    success_url = reverse_lazy('ajustes:subscribers_list')

class MeasurerDeleteView(DeleteView):
    model = Measurer
    success_url = reverse_lazy('ajustes:measurer_list')

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