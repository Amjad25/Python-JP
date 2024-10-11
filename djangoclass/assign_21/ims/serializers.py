from rest_framework import serializers


class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True, max_length=500)


        
class SupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    contact_info = serializers.CharField(required=True, max_length=500)




class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True, max_length=100)
    description = serializers.CharField(required=True, max_length=500)
    price = serializers.DecimalField(required=True, max_digits=10, decimal_places=2)
    quantity = serializers.IntegerField(required=True)
    category_id = serializers.IntegerField(required=True)
    suppliers = serializers.ListField(child=serializers.IntegerField(), required=True)







    

