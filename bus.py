"""Bus class mapped to the buses table."""


class Bus:
    """Represents a physical bus assigned to a service schedule."""
    # Bus belongs to one Service and one BusModel.
    # NOTE: Weekend/workday assignment controls which capacity applies by date.

    # initialize a bus entity matching the buses table structure
    def __init__(self, bus_id: int, service_id: int, bus_model_id: int, schedule_type: str):
        """Store bus identity, service link, model link, and schedule type."""
        self.id = bus_id
        self.service_id = service_id
        self.bus_model_id = bus_model_id
        self.schedule_type = schedule_type
