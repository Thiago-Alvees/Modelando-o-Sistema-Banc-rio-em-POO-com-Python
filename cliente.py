from conta import Conta

class Cliente:
    """
    Classe que representa um cliente do banco.

    Atributos:
        endereco (str): Endereço do cliente.
        contas (list): Lista de contas associadas ao cliente.
    """
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        """
        Realiza uma transação em uma conta.

        Args:
            conta (Conta): Conta na qual a transação será realizada.
            transacao (Transacao): Transação a ser realizada.
        """
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        """
        Adiciona uma conta à lista de contas do cliente.

        Args:
            conta (Conta): Conta a ser adicionada.
        """
        self.contas.append(conta)


class PessoaFisica(Cliente):
    """
    Classe que representa um cliente pessoa física.

    Atributos:
        nome (str): Nome do cliente.
        data_nascimento (str): Data de nascimento do cliente.
        cpf (str): CPF do cliente.
    """
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
