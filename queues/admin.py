from django.contrib import admin
from .models import ServiceCategory, Counter, QueueItem, BankConfig

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'prefix', 'color')

@admin.register(Counter)
class CounterAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_category', 'current_petugas', 'is_active')
    list_filter = ('service_category', 'is_active')

@admin.register(QueueItem)
class QueueItemAdmin(admin.ModelAdmin):
    list_display = ('formatted_number', 'category', 'status', 'counter', 'petugas', 'created_at')
    list_filter = ('status', 'category', 'counter')
    search_fields = ('number',)

@admin.register(BankConfig)
class BankConfigAdmin(admin.ModelAdmin):
    list_display = ('bank_name', 'is_open')
