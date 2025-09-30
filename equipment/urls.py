from django.urls import path
from . import views

app_name = 'equipment'

urlpatterns = [
    path('login/', views.custom_login, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('equipment/', views.equipment_list, name='equipment_list'),
    path('my/', views.my_equipment, name='my_equipment'),
    path('create/', views.equipment_create, name='equipment_create'),
    path('<int:pk>/', views.equipment_detail, name='equipment_detail'),
    path('<int:pk>/edit/', views.equipment_update, name='equipment_update'),
    path('<int:pk>/delete/', views.equipment_delete, name='equipment_delete'),
    path('<int:pk>/transfer/', views.equipment_transfer, name='equipment_transfer'),
    path('pending-transfers/', views.pending_transfers, name='pending_transfers'),
    path('approve-transfer/<int:transfer_id>/', views.approve_transfer, name='approve_transfer'),
    path('transfer-protocol/<int:transfer_id>/', views.transfer_protocol, name='transfer_protocol'),
    path('export/equipment/', views.export_equipment_excel, name='export_equipment_excel'),
    path('export/transfers/', views.export_transfers_excel, name='export_transfers_excel'),
] 