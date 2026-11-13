from abc import ABC, abstractmethod

# Abstract Base Class acting as an Interface / Contract
class PaymentGateway(ABC):
    @abstractmethod
    def process_payment(self, amount: float) -> None:
        """Every payment method must implement this method."""
        pass


# Realization: CreditCardPayment implements the PaymentGateway contract
class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ₹{amount} securely via Credit Card.")


# Realization: UPIPayment implements the PaymentGateway contract
class UPIPayment(PaymentGateway):
    def process_payment(self, amount: float) -> None:
        print(f"Processing ₹{amount} instantly via UPI.")


# Usage
# payment: PaymentGateway = PaymentGateway()  # TypeError: Cannot instantiate abstract class

cc_payment: PaymentGateway = CreditCardPayment()
cc_payment.process_payment(1500.0)

upi_payment: PaymentGateway = UPIPayment()
upi_payment.process_payment(450.0)