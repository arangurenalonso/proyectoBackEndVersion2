from django.urls import path
from .views import CarritoViewSet, PaymentCheckout, CarritoDestroyGetAPIView, OrderAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('', CarritoViewSet.as_view(), name='Carrito de compra'),
    path('<int:id>', CarritoDestroyGetAPIView.as_view(), name='Carrito de compra'),
    path('checkoutpaypal', PaymentCheckout.as_view(),name='Cobro mediante paypal'),
    path('order/<int:id>', OrderAPIView.as_view(), name='obtener una ordern mediante un id'),
]