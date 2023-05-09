from rest_framework import serializers

from .models import Order

class OrderSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%d %B %Y %I:%M %p")

    class Meta:
        model = Order
        fields = '__all__'