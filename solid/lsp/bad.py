"""LSP (Liskov Substitution Principle) — VIOLATION.

Rule (from notes.md): "Objects in a superclass should be replaceable with
objects of a subclass without breaking the correctness or expected behavior
of the application."

`Bird` promises `fly()`. `Penguin` is a `Bird` but overrides `fly()` to raise,
so passing a Penguin to code that accepts a Bird breaks at runtime — exactly
the penguin-in-the-flight-function example from the notes.

Run: python3 bad.py
"""

from __future__ import annotations


class Bird:
    def fly(self) -> str:
        return "flapping through the air"


class Sparrow(Bird):
    pass


class Penguin(Bird):
    def fly(self) -> str:
        raise NotImplementedError("Penguins cannot fly")


def make_bird_fly(bird: Bird) -> None:
    """Trusts Bird's contract — and gets a nasty surprise."""
    print(f"{type(bird).__name__}: {bird.fly()}")


if __name__ == "__main__":
    for bird in (Sparrow(), Penguin()):
        try:
            make_bird_fly(bird)
        except NotImplementedError as exc:
            print(f"BROKEN: {type(bird).__name__} -> {exc}")

    print("\nProblem: the caller did nothing wrong; it trusted the Bird contract,")
    print("but the subclass silently weakened it. Substitution is unsafe.")
