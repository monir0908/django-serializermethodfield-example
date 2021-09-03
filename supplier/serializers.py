from rest_framework import serializers
from .models import Supplier

class SupplierSerializer(serializers.ModelSerializer):

    # serializers.SerializerMethodField()


    class Meta:
        model = Supplier
        fields = ['id', 'supplier_name','supplier_code', 'credit_score']

   

    


  

    