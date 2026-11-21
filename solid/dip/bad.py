"""DIP (Dependency Inversion Principle) — VIOLATION.

Rule (from notes.md): "High-level modules should not depend on low-level
modules. Both should depend on abstractions."

`OrderService` is high-level business logic, but it directly constructs
`MySQLRepository` and `StripeGateway`. Swapping to PostgreSQL or PayPal means
editing the core service and re-testing it; the lamp is hard-wired to one
power plant instead of a wall outlet.

Run: python3 bad.py
"""

from __future__ import annotations


class MySQLRepository:
    def save(self, order_id: str) -> None:
        print(f"[MySQL] saved order {order_id}")


class StripeGateway:
    def charge(self, amount: float) -> str:
        return f"stripe-txn-{int(amount)}"


class OrderService:
    def __init__(self) -> None:
        # Hard-coded low-level details inside the high-level module.
        self.repository = MySQLRepository()
        self.payments = StripeGateway()

    def place_order(self, order_id: str, amount: float) -> str:
        self.repository.save(order_id)
        return self.payments.charge(amount)


if __name__ == "__main__":
    service = OrderService()
    print("transaction:", service.place_order("A-1", 99.0))

    print("\nProblem: using PostgreSQL + PayPal requires rewriting OrderService,")
    print("even though the business rule 'save then charge' did not change.")
