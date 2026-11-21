"""OCP (Open/Closed Principle) — FOLLOWED.

Rule: "Open for extension, closed for modification."

`DiscountCalculator` knows only the abstract `DiscountPolicy`. New behavior is
added by writing a new class, like plugging a new appliance into the wall
socket from the notes — the socket itself is never rewired.

Run: python3 good.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class DiscountPolicy(ABC):
    @abstractmethod
    def discount(self, amount: float) -> float:
        """Return the discount for this policy."""


class RegularDiscount(DiscountPolicy):
    def discount(self, amount: float) -> float:
        return 0.0


class PremiumDiscount(DiscountPolicy):
    def discount(self, amount: float) -> float:
        return amount * 0.10


class VipDiscount(DiscountPolicy):
    def discount(self, amount: float) -> float:
        return amount * 0.20


class GoldDiscount(DiscountPolicy):
    """Extension: added without touching any existing class."""

    def discount(self, amount: float) -> float:
        return amount * 0.30


class DiscountCalculator:
    """Closed for modification: this file never changes for a new customer type."""

    def __init__(self, policy: DiscountPolicy) -> None:
        self.policy = policy

    def discount(self, amount: float) -> float:
        return round(self.policy.discount(amount), 2)


if __name__ == "__main__":
    for policy in (RegularDiscount(), PremiumDiscount(), VipDiscount(), GoldDiscount()):
        name = type(policy).__name__.removesuffix("Discount")
        calculator = DiscountCalculator(policy)
        print(f"{name:8s} -> {calculator.discount(100.0):.2f}")

    print("\nFix: 'gold' was added as GoldDiscount; no existing source was edited.")
