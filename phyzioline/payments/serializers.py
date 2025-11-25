from rest_framework import serializers
from .models import PaymentGatewayConfig, PaymentTransaction


class PaymentGatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentGatewayConfig
        fields = [
            "id",
            "provider",
            "display_name",
            "is_active",
            "metadata",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]


class PaymentTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransaction
        fields = [
            "id",
            "gateway",
            "provider",
            "amount",
            "currency",
            "status",
            "order_reference",
            "customer_email",
            "customer_phone",
            "metadata",
            "provider_response",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "status", "provider_response", "created_at", "updated_at"]


class InitiatePaymentSerializer(serializers.Serializer):
    provider = serializers.ChoiceField(choices=PaymentGatewayConfig.PROVIDER_CHOICES)
    amount = serializers.DecimalField(max_digits=10, decimal_places=2)
    currency = serializers.CharField(max_length=10, default="EGP")
    order_reference = serializers.CharField(max_length=120)
    customer_email = serializers.EmailField(required=False, allow_blank=True)
    customer_phone = serializers.CharField(required=False, allow_blank=True)
    metadata = serializers.DictField(required=False)

