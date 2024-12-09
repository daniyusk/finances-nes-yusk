from datetime import datetime
from finances import Account
from finances import Transaction

DEFAULT_NAME = "Carlos"
DEFAULT_BALANCE = 2059.92
DEFAULT_TRANSACTIONS = [Transaction(200, 1, "Pagamento da comissão.")]

def get_account():
    acc = Account(DEFAULT_NAME)
    acc.balance = DEFAULT_BALANCE
    acc.transactions = DEFAULT_TRANSACTIONS
    return acc

# Testa se está instanciado corretamente
def test_type():
    acc = get_account()
    assert isinstance(acc, Account), "* Não está instanciado a 'Account'."

# Testa se o tipo dos atributos estão corretos
def test_attributes_types():
    acc = get_account()
    assert type(acc.name) is str, "* O tipo do atributo deveria ser str."
    assert type(acc.balance) is float, "* O tipo do atributo deveria ser float."
    assert type(acc.transactions) is list, "* O tipo do atributo deveria ser list."

# Testa se os valores dos atributos estão corretos
def test_attributes_values():
    acc = get_account()
    assert acc.name == DEFAULT_NAME, f"* O valor dado está diferente do que foi atribuído. Deveria ser {DEFAULT_NAME}!"
    assert acc.balance == DEFAULT_BALANCE, f"* O valor dado está diferente do que foi atribuído. Deveria ser {DEFAULT_BALANCE}!"
    assert acc.transactions == DEFAULT_TRANSACTIONS, f"* O valor dado está diferente do que foi atribuído. Deveria ser {DEFAULT_TRANSACTIONS}!"

# Testa se as transações foram feitas corretamente
def test_transaction():
    acc = get_account()
    tr = acc.add_transaction(1000, 2, "Depósito em outro banco.")
    assert tr.amount == 1000, "* Pagamento foi feito de forma incorreta! O valor deveria ser 1000."
    assert tr.category == 2, "* A categoria da transação está incorreta! O valor deveria ser 2."
    assert tr.description == "Depósito em outro banco.", "* A descrição está incorreta! Deveria ser 'Depósito em outro banco.'."
    assert acc.balance == DEFAULT_BALANCE - 1000, "* Pagamento foi feito de forma incorreta! O saldo deveria ser 1059,92."

# Testa se o metódo de transações está correto
def test_get_transactions():
    acc = get_account()
    assert acc.get_transactions() == DEFAULT_TRANSACTIONS, f"* A lista de transações está diferente do que deveria ser. {acc.get_transactions()}"