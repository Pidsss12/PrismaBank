from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('kiosk/', views.kiosk, name='kiosk'),
    path('take-ticket/<int:category_id>/', views.take_ticket, name='take_ticket'),
    path('petugas/', views.petugas_dashboard, name='petugas_dashboard'),
    path('petugas/call-next/', views.call_next, name='call_next'),
    path('petugas/recall-queue/', views.recall_queue, name='recall_queue'),
    path('petugas/complete-queue/', views.complete_queue, name='complete_queue'),
    path('petugas/switch-counter/<int:counter_id>/', views.switch_counter, name='switch_counter'),
    path('dashboard/', views.dashboard_redirect, name='dashboard_redirect'),
    path('customer-portal/', views.customer_portal, name='customer_portal'),
    path('monitor/', views.public_monitor, name='public_monitor'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('admin-dashboard/export/', views.export_queues_csv, name='export_queues_csv'),
    path('admin-dashboard/change-role/<int:user_id>/', views.change_user_role, name='change_user_role'),
    
    # API
    path('queue-status/<int:item_id>/', views.queue_status, name='queue_status'),
    path('api/monitor/', views.api_monitor_data, name='api_monitor_data'),
    path('profile/update/', views.update_profile, name='update_profile'),
    path('logout/', views.user_logout, name='logout'),
]
