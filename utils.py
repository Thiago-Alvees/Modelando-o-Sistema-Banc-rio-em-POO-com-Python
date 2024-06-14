import re
import json

def validar_cpf(cpf):
    """
    Valida o formato do CPF.

    Args:
        cpf (str): CPF a ser validado.

    Returns:
        bool: True se o CPF for válido, False caso contrário.
    """
    return bool(re.match(r'^\d{11}$', cpf))

def validar_valor(valor):
    """
    Valida se o valor é um número positivo.

    Args:
        valor (str): Valor a ser validado.

    Returns:
        bool: True se o valor for positivo, False caso contrário.
    """
    try:
        valor = float(valor)
        return valor > 0
    except ValueError:
        return False

def salvar_dados(clientes, contas, filename="dados.json"):
    """
    Salva os dados de clientes e contas em um arquivo JSON.

    Args:
        clientes (list): Lista de clientes.
        contas (list): Lista de contas.
        filename (str): Nome do arquivo para salvar os dados.
    """
    dados = {
        "clientes": [cliente.__dict__ for cliente in clientes],
        "contas": [conta.__dict__ for conta in contas]
    }
    with open(filename, "w") as f:
        json.dump(dados, f)

def carregar_dados(filename="dados.json"):
    """
    Carrega os dados de clientes e contas de um arquivo JSON.

    Args:
        filename (str): Nome do arquivo para carregar os dados.

    Returns:
        tuple: Tupla contendo a lista de clientes e a lista de contas.
    """
    with open(filename, "r") as f:
        dados = json.load(f)
    # Reconstruir objetos a partir dos dados carregados
    return dados["clientes"], dados["contas"]
