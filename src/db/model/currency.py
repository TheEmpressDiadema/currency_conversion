from typing import Optional
from dataclasses import dataclass


@dataclass
class Currency:
    id: Optional[int]
    code: str
    full_name: str
    sign: str
    created: str
    updated: str

    def __str__(self):
        return str({
            "id": self.id,
            "code": self.code,
            "full_name": self.full_name,
            "sign": self.sign,
            "created": self.created,
            "updated": self.updated
        })