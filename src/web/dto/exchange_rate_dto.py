from typing import Optional
from dataclasses import dataclass, asdict

from src.db.model.exchange_rate import ExchangeRate

@dataclass
class ExchangeRateDto:
    id: Optional[int]
    base_currency_id: int
    target_currency_id: int
    rate: float
    created: str
    updated: str

    def __str__(self):
        return str(asdict(self))
    
    @classmethod
    def from_model(cls, model: ExchangeRate):
        return ExchangeRateDto(model.id, model.base_currency_id, model.target_currency_id,
                               model.rate, model.created, model.updated)