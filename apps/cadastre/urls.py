from django.contrib import admin
from django.urls import path
from .views import (
    SubscribersListView,
    SubscribersDetailView,
    SubscribersCreateView,
    SubscribersUpdateView,
    SubscribersDeleteView,
    MeasurerListView,
    MeasurerDetailView,
    MeasurerCreateView,
    MeasurerUpdateView,
    MeasurerDeleteView,
    CadastralListView,
    CadastralDetailView,
    CadastralCreateView,
    CadastralUpdateView,
    CadastralDeleteView,

    ReportSubscribersExcel,
    )

cadastre_patterns = ([
    path('subscribers_list/', SubscribersListView.as_view(), name="subscribers_list"),
    path('subscribers_list_table/', SubscribersListView.as_view(template_name="configuration/subscribers_list_tabla.html"), name="subscribers_list_table"),
    path('subscribers_detail/<int:pk>/', SubscribersDetailView.as_view(), name="subscribers_detail"),
    path('subscribers_create/', SubscribersCreateView.as_view(), name="subscribers_create"),
    path('subscribers_update/<int:pk>/', SubscribersUpdateView.as_view(), name="subscribers_update"),
    path('subscribers_delete/<int:pk>/', SubscribersDeleteView.as_view(), name="subscribers_delete"),
    path('subscribers_report/', ReportSubscribersExcel.as_view(), name="subscribers_report"),
    
    path('measurer_list', MeasurerListView.as_view(), name='measurer_list'),
    path('measurer_detail/<int:pk>/', MeasurerDetailView.as_view(), name='measurer_detail'),
    path('measurer_create/', MeasurerCreateView.as_view(), name="measurer_create"),
    path('measurer_update/<int:pk>/', MeasurerUpdateView.as_view(), name="measurer_update"),
    path('measurer_delete/<int:pk>/', MeasurerDeleteView.as_view(), name="measurer_delete"),
    
    path('cadastral_list', CadastralListView.as_view(), name='cadastral_list'),
    path('cadastral_detail/<int:pk>/', CadastralDetailView.as_view(), name='cadastral_detail'),
    path('cadastral_create/', CadastralCreateView.as_view(), name="cadastral_create"),
    path('cadastral_update/<int:pk>/', CadastralUpdateView.as_view(), name="cadastral_update"),
    path('cadastral_delete/<int:pk>/', CadastralDeleteView.as_view(), name="cadastral_delete"),

],'catastro')
