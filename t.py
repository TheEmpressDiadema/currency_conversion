from dataclasses import dataclass
from datetime import datetime

@dataclass
class Currency:
    id: int
    code: str
    full_name: str
    sign: str
    created: str
    updated: str

    def __str__(self):
        return str({
            "id" : self.id,
            "code": self.code,
            "full_name": self.full_name,
            "sign": self.sign,
            "created": self.created,
            "updated": self.updated
        })

if __name__ == "__main__":
    curr = Currency(1, "USD", "United States Dollar", "$", str(datetime.now()), str(datetime.now()))
    print(curr)