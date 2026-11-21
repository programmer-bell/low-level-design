"""SRP (Single Responsibility Principle) — VIOLATION.

Rule (from notes.md): "A class should have one, and only one, reason to change."

`UserManager` mixes three responsibilities:
  1. validating user data       (business rules)
  2. storing users              (persistence)
  3. composing/sending email    (notification)

Why it hurts: changing the email template or switching to SMS forces us to edit
the same class that owns validation and storage. One edit can break unrelated
features, and every new requirement makes the class heavier (the "Swiss Army
Knife" from the notes).

Run: python3 bad.py
"""

from __future__ import annotations


class UserManager:
    """Swiss Army Knife: validation + storage + notification together."""

    def __init__(self) -> None:
        self._users: list[str] = []

    def register(self, name: str, email: str) -> None:
        # --- responsibility 1: validation ---
        if not name or "@" not in email:
            raise ValueError("Invalid user data")

        # --- responsibility 2: persistence ---
        self._users.append(name)
        print(f"[storage] saved {name!r} (total: {len(self._users)})")

        # --- responsibility 3: notification ---
        # To change this message or channel we must edit register(), which also
        # contains validation and storage code that has nothing to do with it.
        print(f"[email] To: {email}")
        print("[email] Subject: Welcome!")
        print(f"[email] Body: Hello {name}, welcome aboard!")

    def user_count(self) -> int:
        return len(self._users)


if __name__ == "__main__":
    manager = UserManager()
    manager.register("Alice", "alice@example.com")
    print("users:", manager.user_count())

    print("\nProblem: switching email -> SMS requires editing register(),")
    print("which also owns validation and storage. Three reasons to change.")
