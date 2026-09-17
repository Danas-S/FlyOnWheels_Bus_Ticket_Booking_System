"""User class mapped to the users table."""


class User:
    """Represents a system user account."""
    # User owns Ticket records (one-to-many).
    # DEMO NOTE: This mirrors the `user` table used for login and account roles.

    # prompt: initialize a user entity matching the users table structure
    def __init__(self, user_id: int, username: str, password: str, admin: bool):
        """Store core user fields from the database."""
        self.id = user_id
        self.username = username
        self.password = password
        self.admin = admin
