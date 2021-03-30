from rest_framework import serializers
from .models import ShoppingCart, Order, OrderDetail
import simplejson
import json



class CarritoSerializer(serializers.ModelSerializer):
    price=serializers.FloatField(read_only=True)
    class Meta:
        model = ShoppingCart
        fields = ['id', 'curso', 'price']
    def validate(self, attrs):
        return attrs


class PaymentCheckoutSerializer(serializers.Serializer):
    orderID = serializers.CharField(max_length=255, read_only=True)
    
    class Meta:
        fields = ['orderID']

class OrderSerializar(serializers.ModelSerializer):
    orderdetail = serializers.SerializerMethodField()
    def get_orderdetail(self, obj):
        try:
            obj_order_detail=OrderDetail.objects.filter(order__id=obj.id)
            
            lista_order_detail=[]
            for order_detail in obj_order_detail:
                dic_order_detail={
                    'curso':order_detail.curso.name,
                    'price':order_detail.price,
                    'created_at':order_detail.created_at
                }
                lista_order_detail.append(dic_order_detail)
            #Convierto la lista en un tipo string
            order_detail_str=json.dumps(lista_order_detail)
            #Deserializar un String 
            order_detail_json=json.loads(order_detail_str)
            return order_detail_json
        except:
            return {
                'falta ingresar dato'
            }


    class Meta:
        model = Order
        fields = ['id', 'price', 'code','created_at','orderdetail']

