from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import PaymentGatewayConfig, PaymentTransaction
from .serializers import (
    PaymentGatewaySerializer,
    PaymentTransactionSerializer,
    InitiatePaymentSerializer,
)
from .services import init_paymob_transaction


class PaymentGatewayViewSet(viewsets.ReadOnlyModelViewSet):
    """Expose active gateways (primarily for frontend config)."""

    queryset = PaymentGatewayConfig.objects.filter(is_active=True)
    serializer_class = PaymentGatewaySerializer
    permission_classes = [IsAuthenticated]


class PaymentTransactionViewSet(viewsets.ModelViewSet):
    queryset = PaymentTransaction.objects.all()
    serializer_class = PaymentTransactionSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=False, methods=["post"], url_path="initiate")
    def initiate_payment(self, request):
        serializer = InitiatePaymentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data

        gateway = get_object_or_404(
            PaymentGatewayConfig, provider=data["provider"], is_active=True
        )

        transaction = PaymentTransaction.objects.create(
            gateway=gateway,
            provider=gateway.provider,
            amount=data["amount"],
            currency=data["currency"],
            status="initiated",
            order_reference=data["order_reference"],
            customer_email=data.get("customer_email", ""),
            customer_phone=data.get("customer_phone", ""),
            metadata=data.get("metadata", {}),
        )

        payment_url = ""
        provider_payload = {}

        if gateway.provider == "paymob":
            payment_url, provider_payload = init_paymob_transaction(gateway, transaction)
        else:
            # Placeholder for other providers
            payment_url = "https://example-payment-provider.com/checkout"

        transaction.provider_response = provider_payload
        transaction.save(update_fields=["provider_response"])

        response = {
            "payment_url": payment_url,
            "transaction": PaymentTransactionSerializer(transaction).data,
        }
        return Response(response, status=status.HTTP_201_CREATED)
