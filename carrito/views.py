from django.shortcuts import render
from rest_framework import generics, views, permissions, viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView, DestroyAPIView,RetrieveDestroyAPIView
from rest_framework.parsers import MultiPartParser, FileUploadParser
from drf_yasg.openapi import Parameter, IN_QUERY, TYPE_STRING
from drf_yasg.utils import swagger_auto_schema
from rest_framework.response import Response
from rest_framework import status

from .serializers import CarritoSerializer, PaymentCheckoutSerializer, OrderSerializar
from .models import ShoppingCart
from authentication.models import User
from app.models import Curso
from .models import ShoppingCart, Order, OrderDetail


from .permissions import IsUser
from .utils import random_code
from .paypal import GetOrder

# Create your views here.
class CarritoViewSet(ListCreateAPIView):
    serializer_class = CarritoSerializer
    queryset = ShoppingCart.objects.all()
    parser_classes = (MultiPartParser, FileUploadParser,)
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        data = request.data
        curso_id=data['curso']
        curso = Curso.objects.get(id=curso_id)
        curso_price=curso.price
        user=self.request.user
        carrito_exist = ShoppingCart.objects.filter(curso=curso_id,user=user)
        print(carrito_exist)
        if carrito_exist.exists():
            return Response({
                'Error': 'Usuario ya ha ingresado el curso al carrito de compra'
            }, status=status.HTTP_302_FOUND)
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=user,price=curso_price)
        carrito_data=serializer.data
        return Response(carrito_data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user) 

class CarritoDestroyGetAPIView(RetrieveDestroyAPIView):
    serializer_class = CarritoSerializer
    permission_classes = (permissions.IsAuthenticated, IsUser, )
    lookup_field = "id"
    
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)  

class OrderAPIView(RetrieveAPIView):
    serializer_class = OrderSerializar
    permission_classes = (permissions.IsAuthenticated, IsUser, )
    lookup_field = "id"
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)  

class PaymentCheckout(generics.GenericAPIView):
    serializer_class = PaymentCheckoutSerializer
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request):
        data_request = request.data
        order_id=data_request['orderID']

        shopping_cart = ShoppingCart.objects.filter(user=request.user).all()
        total_price = round(sum(round((d.price), 2) for d in shopping_cart), 2)

        order = GetOrder().get_order(order_id)
        order_price = float(order.result.purchase_units[0].amount.value)

        if order_price == total_price:
            order_capture = GetOrder().capture_order(order_id, debug=True)

            code = f'PA-{random_code(5)}'
            order = Order.objects.create(price=order_price, user=request.user, code=code)
            if order:
                order_id = order.pk
                for value in shopping_cart:
                    OrderDetail.objects.create(order_id=order_id, curso_id=value.curso.id, price=value.price)
                ShoppingCart.objects.filter(user=request.user).delete()

            data = {
                "id": order_capture.result.id,
                "name": order_capture.result.payer.name.given_name
            }
            return Response(data, status=status.HTTP_201_CREATED)

        return Response({
                'Error': 'Usuario ya ha ingresado el curso al carrito de compra'
            }, status=status.HTTP_302_FOUND)

