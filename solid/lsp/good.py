"""LSP (Liskov Substitution Principle) — FOLLOWED.

Rule: a subclass must honor the parent's contract.

The hierarchy is split by capability:
  - Bird       : what *all* birds can do (walk)
  - FlyingBird : Bird + the `fly()` promise

A Penguin is still a Bird, but it is never offered where flight is required.
Any FlyingBird can be substituted for another without breaking callers.

Run: python3 good.py
"""

from __future__ import annotations


class Bird:
    def walk(self) -> str:
        return "walking on land"


class FlyingBird(Bird):
    def fly(self) -> str:
        return "flapping through the air"


class Sparrow(FlyingBird):
    pass


class Eagle(FlyingBird):
    def fly(self) -> str:
        return "soaring high"


class Penguin(Bird):
    def swim(self) -> str:
        return "swimming in cold water"


def describe(bird: Bird) -> None:
    """Works for every bird — Sparrow, Eagle and Penguin alike."""
    print(f"{type(bird).__name__}: {bird.walk()}")


def make_bird_fly(bird: FlyingBird) -> None:
    """Only asks for the capability it actually needs."""
    print(f"{type(bird).__name__}: {bird.fly()}")


if __name__ == "__main__":
    for bird in (Sparrow(), Eagle(), Penguin()):
        describe(bird)

    print()
    for bird in (Sparrow(), Eagle()):
        make_bird_fly(bird)

    print("\nFix: no fake fly() on Penguin, no runtime surprise; every FlyingBird")
    print("is a safe substitute. Type checkers also reject a Penguin passed here.")
