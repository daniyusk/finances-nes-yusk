from datetime import datetime
from finances import Account
from finances import Investment
from finances.investment import TYPES
from finances import Client

DEFAULT_TYPE = 1
DEFAULT_AMOUNT = 500
DEFAULT_RATE = 0.02

def get_investment():
    inv = Investment(DEFAULT_TYPE, DEFAULT_AMOUNT, DEFAULT_RATE)
    inv.client = Client("Ana Beatriz")
    return inv

# Testa se está instanciado corretamente
def test_type():
    inv = get_investment()
    assert isinstance(inv, Investment), "* Não está instanciado a 'Account'."

# Testa se o tipo dos atributos estão corretos
def test_attributes_types():
    inv = get_investment()
    assert type(inv.type) is str, "* O tipo do atributo deveria ser str."
    assert type(inv.initial_amount) is float, "* O tipo do atributo deveria ser float."
    assert type(inv.date_purchased) is datetime, "* O tipo do atributo deveria ser datetime."
    assert type(inv.rate_of_return) is float, "* O tipo do atributo deveria ser float."
    assert type(inv.client) is Client, "* O tipo do atributo deveria ser Client."

# Testa se os valores dos atributos estão corretos
def test_attributes_values():
    inv = get_investment()
    assert inv.type == TYPES[DEFAULT_TYPE], f"* O valor dado está diferente do que foi atribuído. Deveria ser {TYPES[DEFAULT_TYPE]}!"
    assert inv.initial_amount == DEFAULT_AMOUNT, f"* O valor dado está diferente do que foi atribuído. Deveria ser {DEFAULT_AMOUNT}!"
    assert inv.rate_of_return == DEFAULT_RATE, f"* O valor dado está diferente do que foi atribuído. Deveria ser {DEFAULT_RATE}!"