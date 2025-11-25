from django.contrib import admin
from .models import PaymentGatewayConfig, PaymentTransaction


@admin.register(PaymentGatewayConfig)
class PaymentGatewayConfigAdmin(admin.ModelAdmin):
    list_display = ("display_name", "provider", "is_active", "created_at")
    list_filter = ("provider", "is_active")
    search_fields = ("display_name", "provider")
    readonly_fields = ("created_at", "updated_at")


@admin.register(PaymentTransaction)
class PaymentTransactionAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "provider",
        "amount",
        "currency",
        "status",
        "order_reference",
        "created_at",
    )
    list_filter = ("provider", "status", "currency")
    search_fields = ("order_reference", "customer_email", "customer_phone")
    readonly_fields = ("created_at", "updated_at", "provider_response")
