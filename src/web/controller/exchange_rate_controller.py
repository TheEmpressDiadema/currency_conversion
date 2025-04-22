from src.db.dao.exchange_rate_dao import ExchangeRateDao
from src.web.dto.exchange_rate_dto import ExchangeRateDto

class ExchangeRateController:

    dao: ExchangeRateDao = ExchangeRateDao()

    def get_dto_list(self) -> list[ExchangeRateDto]:
        dto_list = self.dao.get_all()
        return [ExchangeRateDto.from_model(dto) for dto in dto_list]