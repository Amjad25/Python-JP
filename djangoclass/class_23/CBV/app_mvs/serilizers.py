from .models import *
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class SupplierSerilizer(serializers.ModelSerializer):
    class Meta:
        model =Supplier
        fields ='__all__'


class ProductSerilizer(serializers.ModelSerializer):
    # category = CategorySerializer()
    # supplier= SupplierSerilizer(many=True)


    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    supplier= serializers.ManyRelatedField(queryset=Supplier.objects.all(),many =True)
    class Meta:
        model =Product
        fields ='__all__'


