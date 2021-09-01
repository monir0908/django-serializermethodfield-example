from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):

    ranking = serializers.ReadOnlyField()
    class Meta:
        model = Supplier
        fields = '__all__'