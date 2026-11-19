import os
os.system('cls || clear')

saldo = 500
extrato = []

# FUNÇÕES

def limpar_tela():
    os.system('cls || clear')

def ver_saldo(saldo):
    print(f'Saldo disponível: R${saldo}')

def depositar(saldo, extrato):
    print(f'Saldo: R${saldo:.2f}')
    valor = float(input('Digite o valor a ser depositado: '))
    if 0 < valor:
        saldo += valor
        extrato.append(f'Depósito: +R${valor:.2f}')
        print(f'Valor depositado: R${valor:.2f}\nSaldo atual: R${saldo:.2f}')
    else:
        print('Valor inválido.')
    return saldo

def sacar(saldo, extrato):
    print(f'Saldo: R${saldo:.2f}')
    valor = float(input('Digite o valor do saque: '))
    if 0 < valor <= saldo and valor <= 1000:
        saldo -= valor
        extrato.append(f'Saque: -R${valor:.2f}')
        print(f'Saque aprovado.\nSaldo atual: R${saldo:.2f}')
    elif valor <= 0:
        print('Valor inválido. O saque deve ser um valor maior que 0.')
    elif valor > 1000:
        print('Saque negado! O saque deve ser de até R$1000.00.')
    else:
        print('Saldo insuficiente para realizar o saque.')
    return saldo

def ver_extrato(extrato):
    print('\n============= EXTRATO =============')
    if not extrato:
        print('Nenhuma movimentação realizada.')
    else:
        for item in extrato:
            print(item)
    print('=' * 34)

def sair():
    print('Obrigado pela preferência! Volte sempre!')

# MENU

while True:
    print('\n========= BANCO COFRINHO =========')
    print('1 - Ver saldo\n2 - Depositar\n3 - Sacar\n4 - Ver extrato\n0 - Sair')
    print('=' * 34)
    opcao = int(input('\nEscolha a opção desejada: '))

    match opcao:
        case 1:
            ver_saldo(saldo)
        case 2:
            saldo = depositar(saldo, extrato)
        case 3:
            saldo = sacar(saldo, extrato)
        case 4:
            ver_extrato(extrato)
        case 0:
            sair()
            break
        case _:
            print('\nOpção inválida! Digite novamente.')

    input('\nPressione Enter para continuar...')
    limpar_tela()