from dataclasses import dataclass
from datetime import datetime

@dataclass
class Competency:
    id: int
    title: str
    description: str
    status: str
    start_date: datetime
    color: str
    emoji: str