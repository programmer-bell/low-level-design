"""ISP (Interface Segregation Principle) — VIOLATION.

Rule (from notes.md): "A client should never be forced to implement an
interface that it does not use."

`Machine` is one fat interface: print + scan + fax. A `SimplePrinter` is
forced to implement all three, so it carries dead methods that just raise.
Callers see a `Machine` and cannot tell which operations really work — the
office-printer problem from the notes.

Run: python3 bad.py
"""

from __future__ import annotations

from abc import ABC, abstractmethod


class Machine(ABC):
    @abstractmethod
    def print(self, document: str) -> None: ...

    @abstractmethod
    def scan(self) -> str: ...

    @abstractmethod
    def fax(self, number: str, document: str) -> None: ...


class SimplePrinter(Machine):
    def print(self, document: str) -> None:
        print(f"[print] {document}")

    def scan(self) -> str:
        raise NotImplementedError("this device has no scanner")

    def fax(self, number: str, document: str) -> None:
        raise NotImplementedError("this device has no fax modem")


class MultiFunctionPrinter(Machine):
    def print(self, document: str) -> None:
        print(f"[print] {document}")

    def scan(self) -> str:
        return "scanned page"

    def fax(self, number: str, document: str) -> None:
        print(f"[fax] {document} -> {number}")


def send_fax(machine: Machine, number: str, document: str) -> None:
    # The type says this is fine; for SimplePrinter it is a runtime landmine.
    machine.fax(number, document)


if __name__ == "__main__":
    printer = SimplePrinter()
    printer.print("Invoice")

    try:
        send_fax(printer, "555-0100", "Invoice")
    except NotImplementedError as exc:
        print(f"BROKEN: {exc}")

    print("\nProblem: SimplePrinter implements methods it cannot support, and")
    print("send_fax() only discovers the truth at runtime.")
