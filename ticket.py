"""Ticket class mapped to the tickets table."""


class Ticket:
    """Represents a booking owned by a user for a specific run."""
    # Ticket links one User to one Run (booking relationship).
    # NOTE: In Part 2, `number` stores quantity in one booking row.

    # initialize a ticket entity matching the tickets table structure
    def __init__(self, ticket_id: int, user_id: int, run_id: int, seat_number: int):
        """Store ticket identity, owner, run, and seat assignment."""
        self.id = ticket_id
        self.user_id = user_id
        self.run_id = run_id
        self.seat_number = seat_number
