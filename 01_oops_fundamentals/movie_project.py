"""A simple movie ticket booking program.

Concepts covered:
- Classes and objects
- Constructor (__init__) with input validation
- Normal attributes vs. a derived value (@property)
- Methods that validate input and return True/False
- __str__ for readable object output
"""


class Movie:
    """Represents one movie and its seat booking state."""

    def __init__(self, movie_name: str, total_seats: int, ticket_price: float) -> None:
        # Validate the data before storing it.
        if not movie_name.strip():
            raise ValueError("Movie name cannot be empty")
        if total_seats <= 0:
            raise ValueError("Total seats must be greater than 0")
        if ticket_price <= 0:
            raise ValueError("Ticket price must be greater than 0")

        self.movie_name = movie_name.strip()
        self.total_seats = total_seats          # never changes
        self.ticket_price = float(ticket_price)
        self.booked_seats = 0
        self.earnings = 0.0

    @property
    def available_seats(self) -> int:
        """Seats still free. Calculated from the other two values."""
        return self.total_seats - self.booked_seats

    def book_tickets(self, num_of_tickets: int) -> bool:
        """Book tickets. Returns True on success, False otherwise."""
        if num_of_tickets <= 0:
            print("Please enter a valid number of tickets (1 or more).")
            return False

        if num_of_tickets > self.available_seats:
            print(f"Sorry, only {self.available_seats} seat(s) available.")
            return False

        total_price = self.ticket_price * num_of_tickets
        self.booked_seats += num_of_tickets
        self.earnings += total_price

        print(f"Booked {num_of_tickets} ticket(s) for {self.movie_name}.")
        print(f"Total price = {total_price:.2f}")
        return True

    def cancel_tickets(self, num_of_tickets: int) -> bool:
        """Cancel booked tickets and refund the money. Returns True on success."""
        if num_of_tickets <= 0:
            print("Please enter a valid number of tickets (1 or more).")
            return False

        if num_of_tickets > self.booked_seats:
            print(f"You can cancel at most {self.booked_seats} ticket(s).")
            return False

        refund = self.ticket_price * num_of_tickets
        self.booked_seats -= num_of_tickets
        self.earnings -= refund

        print(f"Cancelled {num_of_tickets} ticket(s). Refund = {refund:.2f}")
        return True

    def show_status(self) -> None:
        """Print the current state of the movie."""
        print(f"Movie name      = {self.movie_name}")
        print(f"Ticket price    = {self.ticket_price:.2f}")
        print(f"Total seats     = {self.total_seats}")
        print(f"Seats available = {self.available_seats}")
        print(f"Total booked    = {self.booked_seats}")
        print(f"Earnings        = {self.earnings:.2f}")

    def __str__(self) -> str:
        return (
            f"{self.movie_name} "
            f"({self.available_seats}/{self.total_seats} seats available)"
        )


def main() -> None:
    movie = Movie("Alume", 120, 599)

    print(movie)
    movie.show_status()

    movie.book_tickets(70)
    movie.show_status()

    movie.book_tickets(70)   # fails: only 50 seats left
    movie.book_tickets(0)    # fails: invalid count
    movie.cancel_tickets(20)  # refund 20 tickets
    movie.show_status()

    print(movie)


if __name__ == "__main__":
    main()
