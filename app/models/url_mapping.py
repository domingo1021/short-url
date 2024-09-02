"""
UrlMapping entity that contains the original URL, short URL, expiration date, created date, and expiration duration.
"""
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone

@dataclass()
class UrlMapping:
    """
    UrlMapping entity with properties:
    - original_url: The original URL.
    - short_url: The short URL.
    - created_at: The created date of the short URL.
    - expiration_date: The expiration date of the short URL. (now + 30 days)
    - expiration_duration_day: The duration of the short URL expiration in days.
    """
    original_url: str
    short_url: str = field(init=False)
    expiration_date: datetime = field(init=False)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    expiration_duration_day: int = 30

    def __post_init__(self):
        self.expiration_date = self.created_at + timedelta(days=self.expiration_duration_day)

    def is_expired(self) -> bool:
        """ Check if the URL mapping is expired. """
        return datetime.now(timezone.utc) > self.expiration_date
