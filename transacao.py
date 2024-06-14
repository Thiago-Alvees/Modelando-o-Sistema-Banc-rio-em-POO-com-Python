from abc import ABC, abstractmethod

class Transacao(ABC):
    """
    Classe abstrata que representa uma transação bancária.
    """
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):
    """
    Classe que representa um saque.

    Atributos:
        valor (float): Valor do saque.
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    """
    Classe que representa um depósito.

    Atributos:
        valor (float): Valor do depósito.
    """
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)
        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
