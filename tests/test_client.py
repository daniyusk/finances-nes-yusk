from finances import Client
from finances import Account
from finances import Investment

DEFAULT_NAME = "Maria Clara"

def get_client():
    return Client(DEFAULT_NAME)

# Testa se está instanciado corretamente
def test_type():
    client = get_client()
    assert isinstance(client, Client), "* Não está instanciado a 'Account'."

# Testa se o tipo dos atributos estão corretos
def test_attributes_types():
    client = get_client()
    assert type(client.name) is str, "* O tipo do atributo deveria ser str."
    assert type(client.accounts) is list, "* O tipo do atributo deveria ser list."
    assert type(client.investments) is list, "* O tipo do atributo deveria ser list."

# Testa se os valores dos atributos estão corretos
def test_attributes_values():
    client = get_client()
    acc = client.add_acount(DEFAULT_NAME)

    assert client.name == DEFAULT_NAME, f"* O valor dado está diferente do que foi atribuído. Deveria ser {DEFAULT_NAME}!"
    assert client.accounts == [acc], f"* O valor dado está diferente do que foi atribuído. Deveria ser {[acc]}!"

    inv = Investment(1, 200, 0.1)
    client.add_investment(inv)
    assert client.investments == [inv], f"* O valor dado está diferente do que foi atribuído. Deveria ser {[inv]}!"