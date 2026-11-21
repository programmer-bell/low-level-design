"""OCP (Open/Closed Principle) — VIOLATION.

Rule (from notes.md): "Software entities should be open for extension, but
closed for modification."

`DiscountCalculator.discount()` branches on a customer-type string. Adding a
new type (e.g. "gold") means editing the existing, already-working method:
every new feature re-opens the code branch where old bugs can creep in.

Run: python3 bad.py
"""

from __future__ import annotations


class DiscountCalculator:
    def discount(self, customer_type: str, amount: float) -> float:
        # Adding a type requires modifying THIS method — not an extension.
        if customer_type == "regular":
            rate = 0.0
        elif customer_type == "premium":
            rate = 0.10
        elif customer_type == "vip":
            rate = 0.20
        else:
            raise ValueError(f"Unknown customer type: {customer_type!r}")
        return round(amount * rate, 2)


if __name__ == "__main__":
    calculator = DiscountCalculator()
    for customer_type in ("regular", "premium", "vip"):
        print(f"{customer_type:8s} -> {calculator.discount(customer_type, 100.0):.2f}")

    print("\nProblem: a new 'gold' customer currently explodes:")
    try:
        print(calculator.discount("gold", 100.0))
    except ValueError as exc:
        print(f"  ValueError: {exc}")
    print("To support it we must edit discount() and re-test all existing branches.")
