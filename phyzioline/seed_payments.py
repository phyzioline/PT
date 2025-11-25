import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "phyzioline_core.settings")
django.setup()

from payments.models import PaymentGatewayConfig


def main():
    PaymentGatewayConfig.objects.update_or_create(
        provider="paymob",
        defaults={
            "display_name": "Paymob Egypt",
            "api_key": "PAYMOB_TEST_API_KEY",
            "hmac_secret": "PAYMOB_HMAC_SECRET",
            "integration_id": "123456",
            "iframe_id": "7890",
            "metadata": {"note": "Replace with real credentials in production."},
        },
    )
    print("✅ Paymob gateway placeholder created.")


if __name__ == "__main__":
    main()

