from typing import Optional
from dataclasses import dataclass, asdict

from src.db.model.currency import Currency

@dataclass
class CurrencyDto:
    id: Optional[int]
    code: str
    full_name: str
    sign: str
    created: str
    updated: str

    def __str__(self):
        return str(asdict(self))
    
    @classmethod
    def from_model(cls, model: Currency):
        return CurrencyDto(model.id, model.code, model.full_name, 
                           model.sign, model.created, model.updated)