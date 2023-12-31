from datetime import date

#DATA
hoje = date.today()

#SALDO
saldo = 1000.00

#SAQUE
LIMITE_SAQUE = 500.00
SAQUE_DIARIO = 3
count_saque = 0
valor_sacado = []

#DEPOSITO
valor_depositado = []

#EXTRATO
extrato_saque = []
extrato_deposito = []
total_extrato_saque = 0
total_extrato_deposito = 0


#   VALIDAR DATA DE HOJE, RENOVAR LIMITE DE SAQUE DIARIO CASO OCORRA VIRADA DA DATA
if hoje != date.today():
    count_saque = 0

#FUNÇÕES SACAR, DEPOSITAR, VISUALIZAR_EXTRATO_SAQUE E VISUALIZAR_EXTRATO_DEPOSITO

def sacar(valor):
    global saldo, count_saque, valor_sacado, extrato_saque, total_extrato_saque #declarando 'saldo' como variável global
    if isinstance(valor, int):
        if valor <= saldo:
            if valor <= LIMITE_SAQUE:
                if count_saque <= SAQUE_DIARIO:
                    saldo -= valor
                    valor_sacado.append(valor)
                    extrato_saque.append(valor_sacado)
                    total_extrato_saque += valor
                    count_saque += 1
                    print("SAQUE REALIZADO.")
                else:
                    print("LIMITE DE 3 SAQUES DIARIOS ATINGIDOS!")
            else:
                print("NAO E PERMITIDO VALOR ACIMA DE R$ 500.00 POR OPERAÇÃO DE SAQUE.")
        else:
            print("SALDO INSUFICIENTE.")
    else:
        print("VALOR INVÁLIDO!")

def depositar(valor):
    global saldo, valor_depositado, extrato_deposito, total_extrato_deposito #declarando 'saldo' como variável global
    if isinstance(valor, int):
        if valor > 0:
            saldo += valor
            valor_depositado.append(valor)
            extrato_deposito.append(valor_depositado)
            total_extrato_deposito += valor
            print("DEPOSITO REALIZADO.")
        else:
            print("VALOR INVÁLIDO!")
    else:
        print("VALOR INVALIDO!")

def visualizar_extrato_saque():
    print(f"==== Extrato - Saques da data: {hoje} ====")
    n = 0
    for extrato in extrato_saque:
        print(f"Saque de R$ {extrato[n]} realizado na data {hoje}.")
        n += 1
    #ALTERNATIVA À MINHA SOLUÇÃO, SUGERIDA POR CHATGPT, USANDO 'enumerate'
    '''
    for i, extrato in enumerate(extrato_saque, 1):
        print(f"Saque {i} de R$ {extrato} realizado na data {hoje}.")
    '''
    print(f"Saldo total: R$ {saldo}")

def visualizar_extrato_deposito():
    print(f"==== Extrato - Depositos da data: {hoje} ====")
    n = 0
    for extrato in extrato_deposito:
        print(f"Deposito de R$ {extrato[n]} realizado na data {hoje}.")
        n += 1
    print(f"Saldo total: R$ {saldo}")



#OPÇÕES
texto_opções = """
=== SEJA BEM-VINDO! ===
=== SELECIONE OPÇÃO DESEJADA ===
[0] EXIBIR EXTRATO DE DEPOSITOS
[1] EXIBIR EXTRATO DE SAQUES
[2] REALIZAR SAQUE
[3] REALIZAR DEPOSITO
[4] SAIR
"""
print(texto_opções)
opcao = "0"
while(opcao != 4):
    opcao = input("DIGITE NÚMERO DA OPÇÃO DESEJADA: ")
    if opcao == "0":
        print("OPÇÃO SELECIONADA - [0] EXIBIR EXTRATO DE DEPOSITOS")
        visualizar_extrato_deposito()
    elif opcao == "1":
        print("OPÇÃO SELECIONADA - [1] EXIBIR EXTRATO DE SAQUES")
        visualizar_extrato_saque()
    elif opcao == "2":
        print("OPÇÃO SELECIONADA - [2] REALIZAR SAQUE")
        valor = int(input("INFORME VALOR A SACAR: R$ "))
        sacar(valor)
    elif opcao == "3":
        print("OPÇÃO SELECIONADA - [3] REALIZAR DEPOSITO")
        valor = int(input("INFORME VALOR A DEPOSITAR: R$ "))
        depositar(valor)
    elif opcao == "4":
        print("OPERAÇÃO FINALIZADA. OBRIGADO!")
        break;
    else:
        print("OPÇÃO INVÁLIDA. SELECIONE OPÇÃO VÁLIDA.")
