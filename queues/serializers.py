from rest_framework import serializers
from .models import QueueItem, ServiceCategory, Counter

class ServiceCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceCategory
        fields = '__all__'

class CounterSerializer(serializers.ModelSerializer):
    service_category_name = serializers.CharField(source='service_category.name', read_only=True)
    class Meta:
        model = Counter
        fields = '__all__'

class QueueItemSerializer(serializers.ModelSerializer):
    formatted_number = serializers.CharField(read_only=True)
    category_name = serializers.CharField(source='category.name', read_only=True)
    counter_name = serializers.CharField(source='counter.name', read_only=True, allow_null=True)
    
    class Meta:
        model = QueueItem
        fields = '__all__'
