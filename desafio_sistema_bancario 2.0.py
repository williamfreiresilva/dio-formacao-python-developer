from datetime import date

# DATA
hoje = date.today()

dado_conta = {
    # SALDO
    'saldo': 1000.00,

    # SAQUE
    'LIMITE_SAQUE': 500.00,
    'SAQUE_DIARIO': 3,
    'count_saque': 0,
    'valor_sacado': [],

    # DEPÓSITO
    'valor_depositado': [],

    # EXTRATO
    'extrato_saque': [],
    'extrato_deposito': [],
    'total_extrato_saque': 0,
    'total_extrato_deposito': 0
}

# ATRIBUTOS DO USUÁRIO
usuario = {
    'nome': [],
    'data_de_nascimento': [],
    'cpf': [],
    'endereco': {
        'quadra': [],
        'conjunto': [],
        'numero': [],
        'cidade': [],
        'uf': [],
        'cep': []
    }
}

# ATRIBUTOS DA CONTA CORRENTE
conta_corrente = {
    'agencia': ['0001'],
    'conta': [0],
    'usuario': [usuario]
}

# VALIDAR DATA DE HOJE, RENOVAR LIMITE DE SAQUE DIARIO CASO OCORRA VIRADA DA DATA
if hoje != date.today():
    dado_conta['count_saque'] = 0

# ATUALIZAÇÃO VERSÃO 2 DO CÓDIGO: INCLUSÃO DE FUNÇÃO CRIAR_USUARIO
def criar_usuario(*, cpf, nome, data_de_nascimento, quadra, conjunto, numero, cidade, uf, cep):
    usuario['cpf'].append(cpf)
    usuario['nome'].append(nome)
    usuario['data_de_nascimento'].append(data_de_nascimento)
    usuario['endereco']['quadra'].append(quadra)
    usuario['endereco']['conjunto'].append(conjunto)
    usuario['endereco']['numero'].append(numero)
    usuario['endereco']['cidade'].append(cidade)
    usuario['endereco']['uf'].append(uf)
    usuario['endereco']['cep'].append(cep)

# ATUALIZAÇÃO VERSÃO 2 DO CÓDIGO: INCLUSÃO DE FUNÇÃO CRIAR_CONTA_CORRENTE
def criar_conta_corrente(*, usuario):
    conta_corrente['conta'][0] += 1  # Increment account number
    conta_corrente['usuario'].append(usuario)

# FUNÇÕES SACAR
def sacar(dado_conta, valor):
    if isinstance(valor, int):
        if valor <= dado_conta['saldo']:
            if valor <= dado_conta['LIMITE_SAQUE']:
                if dado_conta['count_saque'] < dado_conta['SAQUE_DIARIO']:
                    dado_conta['saldo'] -= valor
                    dado_conta['valor_sacado'].append(valor)
                    dado_conta['extrato_saque'].append(valor)
                    dado_conta['total_extrato_saque'] += valor
                    dado_conta['count_saque'] += 1
                    print("SAQUE REALIZADO.")
                else:
                    print("LIMITE DE 3 SAQUES DIÁRIOS ATINGIDOS!")
            else:
                print("NÃO É PERMITIDO VALOR ACIMA DE R$ 500.00 POR OPERAÇÃO DE SAQUE.")
        else:
            print("SALDO INSUFICIENTE.")
    else:
        print("VALOR INVÁLIDO!")
# FUNÇÃO DEPOSITAR
def depositar(dado_conta, valor, /):
    if isinstance(valor, int):
        if valor > 0:
            dado_conta['saldo'] += valor
            dado_conta['valor_depositado'].append(valor)
            dado_conta['extrato_deposito'].append(valor)
            dado_conta['total_extrato_deposito'] += valor
            print("DEPÓSITO REALIZADO.")
        else:
            print("VALOR INVÁLIDO!")
    else:
        print("VALOR INVÁLIDO!")
# FUNÇÃO VISUALIZAR_EXTRATO_SAQUE
def visualizar_extrato_saque(dado_conta, /):
    print(f"==== Extrato - Saques da data: {hoje} ====")
    for extrato in dado_conta['extrato_saque']:
        print(f"Saque de R$ {extrato} realizado na data {hoje}.")
    print(f"Saldo total: R$ {dado_conta['saldo']}")

# FUNÇÃO VISUALIZAR_EXTRATO_DEPOSITO
def visualizar_extrato_deposito(dado_conta, /):
    print(f"==== Extrato - Depósitos da data: {hoje} ====")
    for extrato in dado_conta['extrato_deposito']:
        print(f"Depósito de R$ {extrato} realizado na data {hoje}.")
    print(f"Saldo total: R$ {dado_conta['saldo']}")

# FUNÇÃO VALIDAR_CPF_NOVO_USUARIO
def validar_cpf_novo_usuario(cpf):
    if cpf not in usuario['cpf']:
        novo_usuario = criar_usuario(
            cpf=cpf,
            nome=input('Informe o nome completo: '),
            data_de_nascimento=input('Informe a data de nascimento: '),
            quadra=input('Endereço - informe o número ou nome da quadra: '),
            conjunto=input('Endereço - informe o conjunto: '),
            numero=input('Endereço - informe o número do lote: '),
            cidade=input('Endereço - informe a cidade: '),
            uf=input('Endereço - informe a UF (estado): '),
            cep=input('Endereço - informe o CEP: ')
        )
        # Append the new user to the usuario dictionary
        usuario['nome'].append(novo_usuario['nome'])
        usuario['data_de_nascimento'].append(novo_usuario['data_de_nascimento'])
        usuario['cpf'].append(novo_usuario['cpf'])
        usuario['endereco']['quadra'].append(novo_usuario['endereco']['quadra'])
        usuario['endereco']['conjunto'].append(novo_usuario['endereco']['conjunto'])
        usuario['endereco']['numero'].append(novo_usuario['endereco']['numero'])
        usuario['endereco']['cidade'].append(novo_usuario['endereco']['cidade'])
        usuario['endereco']['uf'].append(novo_usuario['endereco']['uf'])
        usuario['endereco']['cep'].append(novo_usuario['endereco']['cep'])

        criar_conta_corrente(usuario=novo_usuario)
    else:
        print('Usuário já cadastrado no nosso sistema.')

# FUNÇÃO VALIDAR_CPF_CLIENTE
def validar_cpf_cliente(cpf):
    if cpf in usuario['cpf']:
        criar_conta_corrente(usuario=usuario)
    else:
        while True:
            resposta = input('Usuário não cadastrado. Deseja cadastrar novo usuário? [1] Sim ou [2] Não: ')
            if resposta == '1':
                validar_cpf_novo_usuario(cpf)
                break
            elif resposta == '2':
                print("OPERAÇÃO FINALIZADA. OBRIGADO!")
                break
            else:
                print("Opção inválida. Escolha 1 para Sim ou 2 para Não.")

texto_opcoes = """
=== SEJA BEM-VINDO! ===
=== SELECIONE OPÇÃO DESEJADA ===
[0] EXIBIR EXTRATO DE DEPÓSITOS
[1] EXIBIR EXTRATO DE SAQUES
[2] REALIZAR SAQUE
[3] REALIZAR DEPÓSITO
[4] CRIAR NOVO USUÁRIO
[5] CRIAR NOVA CONTA
[6] SAIR
"""
print(texto_opcoes)

opcao = "0"
while opcao != "6":
    opcao = input("DIGITE NÚMERO DA OPÇÃO DESEJADA: ")

    if opcao == "0":
        print("OPÇÃO SELECIONADA - [0] EXIBIR EXTRATO DE DEPÓSITOS")
        visualizar_extrato_deposito(dado_conta)
    elif opcao == "1":
        print("OPÇÃO SELECIONADA - [1] EXIBIR EXTRATO DE SAQUES")
        visualizar_extrato_saque(dado_conta)
    elif opcao == "2":
        print("OPÇÃO SELECIONADA - [2] REALIZAR SAQUE")
        valor = int(input("INFORME VALOR A SACAR: R$ "))
        sacar(dado_conta, valor)
    elif opcao == "3":
        print("OPÇÃO SELECIONADA - [3] REALIZAR DEPÓSITO")
        valor = int(input("INFORME VALOR A DEPOSITAR: R$ "))
        depositar(dado_conta, valor)
    elif opcao == "4":
        print("OPÇÃO SELECIONADA - [4] CRIAR NOVO USUÁRIO")
        cpf = input('Informe o CPF: ')
        validar_cpf_novo_usuario(cpf)
    elif opcao == "5":
        print("OPÇÃO SELECIONADA - [5] CRIAR NOVA CONTA")
        cpf = input('Informe o CPF do cliente: ')
        validar_cpf_cliente(cpf)
    elif opcao == "6":
        print("OPERAÇÃO FINALIZADA. OBRIGADO!")
    else:
        print("OPÇÃO INVÁLIDA. SELECIONE OPÇÃO VÁLIDA.")

