from datetime import datetime
from finances import Transaction

class Account:
    def __init__(self, name: str) -> None:
        self.name = name
        self.balance = 0.0
        self.transactions = []
        self.client = None

    def add_transaction(self, amount: float, category: int, description: str = "") -> Transaction:
        self.balance -= amount
        tr = Transaction(amount, category, description)
        self.transactions.append(tr)

        return tr

    # Filtra e retorna todas as transações
    def get_transactions(self, start_date: datetime = None, end_date = None, category: int = None) -> list[Transaction]:
        filter_transactions = []

        for tr in self.transactions:
            # Verifica se a categoria é a mesma
            if category == None or tr.category == category:
                # Verifica se a transação foi feita no tempo limite
                if start_date == None or tr.date >= start_date:
                    if end_date == None or tr.date <= end_date:
                        filter_transactions.append(tr)

        # Retorna as transações filtradas
        return filter_transactions