"""Utility services for payment gateways (Paymob-ready)."""
from typing import Tuple, Dict, Any
from .models import PaymentGatewayConfig, PaymentTransaction


def init_paymob_transaction(
    gateway: PaymentGatewayConfig, transaction: PaymentTransaction
) -> Tuple[str, Dict[str, Any]]:
    """
    Placeholder for Paymob integration.
    Returns a tuple (payment_url, provider_payload).
    """

    # TODO: Replace with real Paymob API calls (auth -> order -> payment key -> iframe)
    provider_payload = {
        "amount_cents": int(transaction.amount * 100),
        "currency": transaction.currency,
        "iframe_id": gateway.iframe_id,
        "integration_id": gateway.integration_id,
        "order_reference": transaction.order_reference,
    }
    payment_url = f"https://accept.paymob.com/api/acceptance/iframes/{gateway.iframe_id}?payment_token=MOCK_TOKEN"
    return payment_url, provider_payload

