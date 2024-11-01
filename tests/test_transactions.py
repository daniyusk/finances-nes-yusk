from datetime import datetime
from finances import Transaction
from finances.transaction import CATEGORIES

DEFAULT_AMOUNT = 150.0
DEFAULT_CATEGORY = 2
DEFAULT_DESCRIPTION = "Transferência Teste A"

def get_transaction():
    return Transaction(DEFAULT_AMOUNT, DEFAULT_CATEGORY, DEFAULT_DESCRIPTION)

# Testa se está instanciado corretamente
def test_type():
    tr = get_transaction()
    assert isinstance(tr, Transaction), "* Não está instanciado a 'Transaction'."

# Testa se a categoria existe
def test_category():
    tr = get_transaction()
    assert tr.category in CATEGORIES.keys(), "* Esta categoria está incorreta. Não está localizada no mapeamento."

# Testa se o tipo dos atributos estão corretos
def test_attributes_types():
    tr = get_transaction()
    assert type(tr.amount) is float, "* O tipo do atributo deveria ser float."
    assert type(tr.date) is datetime, "* O tipo do atributo deveria ser datetime."
    assert type(tr.category) is int, "* O tipo do atributo deveria ser int."
    assert type(tr.description) is str, "* O tipo do atributo deveria ser str."

# Testa se os valores dos atributos estão corretos
def test_attributes_values():
    tr = get_transaction()
    assert tr.amount == DEFAULT_AMOUNT, "* O valor dado está diferente do que foi atribuído. Deveria ser 150.0!"
    assert tr.category == DEFAULT_CATEGORY, "* O valor dado está diferente do que foi atribuído. Deveria ser 2!"
    assert tr.description == DEFAULT_DESCRIPTION, "* O valor dado está diferente do que foi atribuído. Deveria ser 'Transferência Teste A'!"

# Testa se os valores atualizam corretamente
def test_update():
    tr = get_transaction()

    tr.update(amount=200.0)
    assert tr.amount == 200.0, "* O valor foi mal atualizado. Deveria ser 200.0!"

    new_date = datetime.now()
    tr.update(date=new_date)
    assert tr.date == new_date, f"* O valor foi mal atualizado. Deveria ser {new_date}!"

    tr.update(category=1)
    assert tr.category == 1, "* O valor foi mal atualizado. Deveria ser 1!"

    tr.update(description="Transferência Teste A")
    assert tr.description == "Transferência Teste A", "* O valor foi mal atualizado. Deveria ser Transferência Teste B!"