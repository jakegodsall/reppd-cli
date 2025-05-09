from datetime import datetime
from dataclasses import dataclass

@dataclass
class Action:
    id: int
    title: str
    description: str
    competency: str
    status: str
    start_date: datetime
    color: str
    emoji: str
