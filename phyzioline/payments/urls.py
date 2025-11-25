from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaymentGatewayViewSet, PaymentTransactionViewSet

router = DefaultRouter()
router.register(r"gateways", PaymentGatewayViewSet, basename="payment-gateway")
router.register(r"transactions", PaymentTransactionViewSet, basename="payment-transaction")

app_name = "payments"

urlpatterns = [
    path("", include(router.urls)),
]

