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
] 