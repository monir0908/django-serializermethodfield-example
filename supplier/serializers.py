from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):

    # rank = serializers.ReadOnlyField(source='ranking')

    health = serializers.SerializerMethodField()

    def get_health(self, obj):
        if obj.score >=20:
            return 'Joss'
        else:
            return 'Not that good'
    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name', 'supplier_code', 'supplier_address', 'score','ranking','health']