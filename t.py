import datetime
from src.db.model.currency import Currency
from src.db.dao.currency_dao import CurrencyDao


curr_time = str(datetime.datetime.today()).split()[0]
currency = Currency(1, "EUR", "EURO", "Э", curr_time, curr_time)
dao = CurrencyDao(r"src\db\data\data.db")
dao.update(currency)