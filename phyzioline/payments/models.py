from django.db import models
from core_data.models import TimeStampedModel


class PaymentGatewayConfig(TimeStampedModel):
    """Stores credentials and settings for payment gateways (Paymob-ready)."""

    PROVIDER_CHOICES = [
        ("paymob", "Paymob"),
        ("stripe", "Stripe"),
        ("paypal", "PayPal"),
        ("manual", "Manual"),
    ]

    provider = models.CharField(max_length=20, choices=PROVIDER_CHOICES, default="paymob")
    display_name = models.CharField(max_length=120, verbose_name="Display Name")
    api_key = models.CharField(max_length=255, verbose_name="API Key / Token")
    hmac_secret = models.CharField(max_length=255, blank=True, verbose_name="HMAC Secret")
    integration_id = models.CharField(max_length=120, blank=True, verbose_name="Integration ID")
    iframe_id = models.CharField(max_length=120, blank=True, verbose_name="Iframe ID")
    is_active = models.BooleanField(default=True, verbose_name="Is Active?")
    metadata = models.JSONField(default=dict, blank=True, verbose_name="Extra Metadata")

    class Meta:
        verbose_name = "Payment Gateway"
        verbose_name_plural = "Payment Gateways"
        ordering = ["provider", "display_name"]

    def __str__(self) -> str:
        return f"{self.display_name} ({self.provider})"


class PaymentTransaction(TimeStampedModel):
    """Internal record for initiated payments."""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("initiated", "Initiated"),
        ("paid", "Paid"),
        ("failed", "Failed"),
        ("refunded", "Refunded"),
    ]

    gateway = models.ForeignKey(
        PaymentGatewayConfig, on_delete=models.SET_NULL, null=True, related_name="transactions"
    )
    provider = models.CharField(max_length=20, choices=PaymentGatewayConfig.PROVIDER_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=10, default="EGP")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    order_reference = models.CharField(max_length=120, blank=True)
    customer_email = models.EmailField(blank=True)
    customer_phone = models.CharField(max_length=30, blank=True)
    metadata = models.JSONField(default=dict, blank=True)
    provider_response = models.JSONField(default=dict, blank=True)

    class Meta:
        verbose_name = "Payment Transaction"
        verbose_name_plural = "Payment Transactions"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.provider} - {self.amount} {self.currency} ({self.status})"
