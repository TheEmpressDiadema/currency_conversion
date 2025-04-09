from dataclasses import dataclass

@dataclass
class ExchangeRate:
    id: int
    base_currency_id: int
    target_currency_id: int
    rate: float
    created: str
    updated: str

    def __str__(self):
        return str({
            "id": self.id,
            "base_currency_id": self.base_currency_id,
            "target_currency_id": self.target_currency_id,
            "created": self.created,
            "updated": self.updated
        })