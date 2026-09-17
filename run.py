"""Run class mapped to the runs table."""


class Run:
    """Represents one dated execution of a service."""
    # Run belongs to one Service and can be referenced by Ticket.
    # NOTE: Runs are generated for 7 days so booking options exist immediately.

    # initialize a run entity matching the runs table structure
    def __init__(self, run_id: int, service_id: int, run_date: str):
        """Store run identity, linked service, and date."""
        self.id = run_id
        self.service_id = service_id
        self.run_date = run_date
