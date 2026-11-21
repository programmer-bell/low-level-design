"""DIP (Dependency Inversion Principle) — FOLLOWED.

Rule: high-level and low-level modules both depend on abstractions.

`OrderService` depends only on the `OrderRepository` and `PaymentGateway`
Protocols. Concrete details (MySQL/Postgres, Stripe/PayPal, in-memory fakes)
are injected from the outside — they satisfy the abstraction, so the core
business logic never changes. This is the "lamp and wall outlet" from the
notes, and it makes testing trivial.

Run: python3 good.py
"""

from __future__ import annotations

from typing import Protocol


# --- abstractions, owned by the high-level side ---
class OrderRepository(Protocol):
    def save(self, order_id: str) -> None: ...


class PaymentGateway(Protocol):
    def charge(self, amount: float) -> str: ...


# --- high-level module: knows nothing about vendors ---
class OrderService:
    def __init__(
        self, repository: OrderRepository, payments: PaymentGateway
    ) -> None:
        self.repository = repository
        self.payments = payments

    def place_order(self, order_id: str, amount: float) -> str:
        self.repository.save(order_id)
        return self.payments.charge(amount)


# --- low-level details: they depend on / satisfy the protocols ---
class MySQLRepository:
    def save(self, order_id: str) -> None:
        print(f"[MySQL] saved order {order_id}")


class PostgresRepository:
    def save(self, order_id: str) -> None:
        print(f"[Postgres] saved order {order_id}")


class StripeGateway:
    def charge(self, amount: float) -> str:
        return f"stripe-txn-{int(amount)}"


class PayPalGateway:
    def charge(self, amount: float) -> str:
        return f"paypal-txn-{int(amount)}"


class InMemoryRepository:
    """A fake for tests — no database needed."""

    def save(self, order_id: str) -> None:
        print(f"[fake repo] recorded {order_id}")


if __name__ == "__main__":
    configs = (
        ("MySQL + Stripe", MySQLRepository(), StripeGateway()),
        ("Postgres + PayPal", PostgresRepository(), PayPalGateway()),
        ("test fake", InMemoryRepository(), StripeGateway()),
    )
    for label, repository, payments in configs:
        service = OrderService(repository, payments)
        print(f"{label}: {service.place_order('A-1', 99.0)}")

    print("\nFix: same OrderService, three different stacks — zero edits to core logic.")
