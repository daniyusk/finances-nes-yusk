from finances import Account
from finances import Investment

class Client:
    def __init__(self, name: str) -> None:
        self.name = name
        self.accounts = []
        self.investments = []

    def add_acount(self, account_name: str) -> Account:
        acc = Account(account_name)
        acc.client = self
        self.accounts.append(acc)

        return acc

    def add_investment(self, investment: Investment) -> None:
        investment.client = self
        self.investments.append(investment)

    # Calcula o saldo das contas juntamente do valor dos investimentos
    def get_net_worth(self) -> float:
        soma = 0

        # Calcula o saldo das contas
        for acc in self.accounts:
            soma += acc.balance

        # Calcula o investimento
        for inv in self.investments:
            soma += inv.calculate_value()

        return soma