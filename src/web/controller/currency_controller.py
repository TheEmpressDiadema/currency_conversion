from src.db.dao.currency_dao import CurrencyDao
from src.web.dto.currency_dto import CurrencyDto

class CurrencyController:

    dao: CurrencyDao = CurrencyDao()

    def get_dto_list(self) -> list[CurrencyDto]:
        dto_list = self.dao.get_all()
        return [CurrencyDto.from_model(dto) for dto in dto_list]