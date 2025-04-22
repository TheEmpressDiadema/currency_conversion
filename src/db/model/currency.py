from typing import Optional
from dataclasses import dataclass, asdict


@dataclass
class Currency:
    id: Optional[int]
    code: str
    full_name: str
    sign: str
    created: str
    updated: str

    def __str__(self):
        return str(asdict(self))