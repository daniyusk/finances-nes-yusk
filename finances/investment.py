from datetime import datetime
from finances import Account

TYPES = {
    1: "Fixa",
    2: "Variável",
    3: "Outros"
}

class Investment():
    def __init__(self, type: int, amount: float, rate_of_return: float) -> None:
        if type not in TYPES.keys():
            raise ValueError("* Tipo inválido!")

        self.date_purchased = datetime.now()
        self.type = TYPES[type]
        self.initial_amount = float(amount)
        self.rate_of_return = rate_of_return
        self.client = None

    def calculate_value(self) -> float:
        diff_date = self.date_purchased - datetime.now()
        months = round(diff_date.days / 30)
        value = self.initial_amount * (1 + self.rate_of_return * months)

        return value

    def sell(self, account: Account) -> None:
        value = self.calculate_value()
        account.balance += value