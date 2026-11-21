"""SRP (Single Responsibility Principle) — FOLLOWED.

Rule: "A class should have one, and only one, reason to change."

Each responsibility has its own home; `RegistrationService` only orchestrates:
  - validation rules  -> UserValidator
  - storage engine    -> UserRepository
  - message template  -> WelcomeNotifier / SmsNotifier
  - registration flow -> RegistrationService

A requirement change now touches exactly one class (the "chef's knife" from
the notes). Bonus: injecting collaborators also keeps the service decoupled.

Run: python3 good.py
"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    name: str
    email: str
    phone: str = ""


class UserValidator:
    def validate(self, user: User) -> None:
        if not user.name or "@" not in user.email:
            raise ValueError("Invalid user data")


class UserRepository:
    def __init__(self) -> None:
        self._users: list[User] = []

    def save(self, user: User) -> None:
        self._users.append(user)
        print(f"[storage] saved {user.name!r} (total: {len(self._users)})")


class WelcomeNotifier:
    def notify(self, user: User) -> None:
        print(f"[email] To: {user.email}")
        print("[email] Subject: Welcome!")
        print(f"[email] Body: Hello {user.name}, welcome aboard!")


class SmsNotifier:
    """New notification channel: no existing class needs to be edited."""

    def notify(self, user: User) -> None:
        print(f"[sms] To: {user.phone} — welcome, {user.name}!")


class RegistrationService:
    """One reason to change: the steps of the registration flow itself."""

    def __init__(
        self,
        validator: UserValidator,
        repository: UserRepository,
        notifier: WelcomeNotifier | SmsNotifier,
    ) -> None:
        self.validator = validator
        self.repository = repository
        self.notifier = notifier

    def register(self, user: User) -> None:
        self.validator.validate(user)
        self.repository.save(user)
        self.notifier.notify(user)


if __name__ == "__main__":
    validator, repository = UserValidator(), UserRepository()

    email_service = RegistrationService(validator, repository, WelcomeNotifier())
    email_service.register(User("Alice", "alice@example.com"))

    sms_service = RegistrationService(validator, repository, SmsNotifier())
    sms_service.register(User("Bob", "bob@example.com", "+1-555-0100"))

    print("\nFix: adding SMS only added a class; validation and storage were untouched.")
