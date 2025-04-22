from typing import Optional
from dataclasses import dataclass, asdict

@dataclass
class ExchangeRate:
    id: Optional[int]
    base_currency_id: int
    target_currency_id: int
    rate: float
    created: str
    updated: str

    def __str__(self):
        return str(asdict(self))