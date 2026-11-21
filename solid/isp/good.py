"""ISP (Interface Segregation Principle) — FOLLOWED.

Rule: split fat interfaces into small, role-based ones so clients depend only
on methods they actually use.

`Printer`, `Scanner` and `FaxMachine` are separate Protocols. A simple printer
implements just `Printer`; a multi-function device combines the roles it
supports. Passing a plain printer to `send_fax()` is now rejected by a type
checker instead of failing in production.

Run: python3 good.py
"""

from __future__ import annotations

from typing import Protocol


class Printer(Protocol):
    def print(self, document: str) -> None: ...


class Scanner(Protocol):
    def scan(self) -> str: ...


class FaxMachine(Protocol):
    def fax(self, number: str, document: str) -> None: ...


class SimplePrinter:
    def print(self, document: str) -> None:
        print(f"[print] {document}")


class MultiFunctionPrinter:
    def print(self, document: str) -> None:
        print(f"[print] {document}")

    def scan(self) -> str:
        return "scanned page"

    def fax(self, number: str, document: str) -> None:
        print(f"[fax] {document} -> {number}")


def send_fax(fax: FaxMachine, number: str, document: str) -> None:
    fax.fax(number, document)


if __name__ == "__main__":
    printer = SimplePrinter()
    printer.print("Invoice")

    multi = MultiFunctionPrinter()
    send_fax(multi, "555-0100", "Invoice")
    print("[scan]", multi.scan())

    print("\nFix: send_fax(printer, ...) no longer type-checks — SimplePrinter")
    print("never promised fax support. No stub methods, no dead dependencies.")
