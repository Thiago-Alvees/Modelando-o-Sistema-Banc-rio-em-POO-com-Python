import textwrap
from cliente import Cliente, PessoaFisica
from conta import ContaCorrente
from transacao import Saque, Deposito
from utils import validar_cpf, validar_valor, salvar_dados, carregar_dados

def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def filtrar_cliente(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return

    for i, conta in enumerate(cliente.contas, start=1):
        print(f"{i}. Conta {conta.numero}")

    escolha = int(input("Escolha a conta: "))
    return cliente.contas[escolha - 1]

def depositar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = input("Informe o valor do depósito: ")
    if not validar_valor(valor):
        print("\n@@@ Valor inválido! @@@")
        return

    valor = float(valor)
    transacao = Deposito(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    valor = input("Informe o valor do saque: ")
    if not validar_valor(valor):
        print("\n@@@ Valor inválido! @@@")
        return

    valor = float(valor)
    transacao = Saque(valor)
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    cliente.realizar_transacao(conta, transacao)

def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado! @@@")
        return

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return

    print("\n================ EXTRATO ================")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("==========================================")

def criar_cliente(clientes):
    cpf = input("Informe o CPF (somente número): ")
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if cliente:
        print("\n@@@ Já existe cliente com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)
    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    if not validar_cpf(cpf):
        print("\n@@@ CPF inválido! @@@")
        return

    cliente = filtrar_cliente(cpf, clientes)
    if not cliente:
        print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
        return

    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)
    print("\n=== Conta criada com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))

def main():
    try:
        clientes, contas = carregar_dados()
    except FileNotFoundError:
        clientes, contas = [], []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)
        elif opcao == "s":
            sacar(clientes)
        elif opcao == "e":
            exibir_extrato(clientes)
        elif opcao == "nu":
            criar_cliente(clientes)
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)
        elif opcao == "lc":
            listar_contas(contas)
        elif opcao == "q":
            salvar_dados(clientes, contas)
            break
        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()
