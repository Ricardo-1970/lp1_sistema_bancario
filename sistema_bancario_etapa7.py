import datetime
import json
import os # Importa o módulo "os" para verificar a existência do arquivo.

nome_arquivo = "banco_dados.json" # Nome do arquivo para salvar os dados.

# Tenta carregar os dados do arquivo se existir.
if os.path.exists(nome_arquivo):
    try:
        with open(nome_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
            saldo = dados.get("saldo", 1000.0) # Carrega o saldo, usa 1000.0 se não encontrar.
            extrato = dados.get("extrato", []) #Carrega extrato usa [] como padrão.
    except Exception as e:
        print(f"Erro ao carregar os dados: {e}. Iniciando com dados padrão.")
        saldo = 1000.0
        extrato = []
else:
    saldo = 1000.0 # Saldo inicial.
    extrato = [] # Lista para armazenar as informações.

def consultar_saldo(): # função adicionada ao código para torná - lo funcional.
    """Exibe o saldo atual. """
    global saldo, extrato
    agora = datetime.datetime.now() # uso da mesma chave - "agora" - .
    extrato.append({"data_hora": agora.strftime("%d/%m/%Y - %H:%M:%S"),"tipo": "Consulta Saldo","valor": saldo}) # dicionário inserido.
    print(f"{agora.strftime('%d/%m/%Y - %H:%M:%S')} - Seu saldo atual é: {saldo:.2f}") # data e hora inserido a consulta de saldo.

def sacar():
    """Realiza as operações de saque,verificando o saldo."""
    global saldo, extrato
    while True:
        try:
            valor_saque = float(input("Digite o valor a sacar: R$ "))
            break
        except ValueError:
            print("Valor inválido. Por favor digite um número.")

    if valor_saque <= saldo:
        saldo -= valor_saque
        agora = datetime.datetime.now() 
        extrato.append({"data_hora": agora.strftime("%d/%m/%Y - %H:%M:%S") ,"tipo": "Saque", "valor": valor_saque})
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso.") 
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insufuciente.")

def depositar():
    """Realiza a operação de depósito.""" 
    global saldo, extrato
    while True:
        try:
            valor_deposito = float(input("Digite o valor a depositar: R$ "))
            break
        except ValueError:
            print("Valor inválido. Por favor digite um número.")
    saldo += valor_deposito
    agora = datetime.datetime.now()
    extrato.append({"data_hora": agora.strftime("%d/%m/%Y - %H:%M:%S") ,"tipo": "Depósito", "valor": valor_deposito})
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.") 
    print(f"Seu novo saldo é: R$ {saldo:.2f}")

def transferir():
    """Realiza a operação de transferência"""
    global saldo, extrato
    while True:
        conta_deposito = input("Digite o numero da conta do destinatário : ")
        if conta_deposito.isdigit():
            break
        else:
            print("Número da conta é inválido. Por favor digite outro número.")

    while True:
        try:
            valor_transferencia = float(input("Digite o valor a transferir: R$  "))
            if valor_transferencia <= 0:
                print("O valor deve ser maior do que zero")
            else:
                break
        except ValueError:
            print("Valor inválido. Por favor digite um número.") 

    if valor_transferencia <= saldo:
        saldo -= valor_transferencia
        agora = datetime.datetime.now() 
        extrato.append({"data_hora": agora.strftime("%d/%m/%Y - %H:%M:%S") ,"tipo": "Transferência", "valor": valor_transferencia})
        print(f"Transferência de R$ {valor_transferencia:.2f} realizada com sucesso para a conta {conta_deposito}") 
        print(f"Seu novo saldo é: R$ {saldo:.2f}")
    else:
        print("Saldo insufuciente.")
     
def exibir_extrato():
    """Exibe o extrato bancário"""
    global extrato
    if not extrato:
        print("Não foram realizadas transações")
    else:
        print("\n --- Extrato Bancário ---")
        for transacao in extrato:
            data_hora = transacao["data_hora"]
            tipo = transacao["tipo"]
            valor = transacao["valor"]
            print(f"{data_hora} - {tipo}: R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")

# . . . (seu código principal com o looping while).
while True:
    print("\n--- Bem - vindo ao se Banco virtual ---")
    print("1 - Consultar Saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Exibir Extrato") 
    print("5 - Transferir")
    print("6 - Sair")

    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1 <= opcao <= 6: 
                 break 
            else:
                print("Opção inválida. Por favor. Digite um número entre 1 e 6.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")

    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4: 
        exibir_extrato()
    elif opcao == 5: # nova condição: transferência
        transferir()    
    elif opcao == 6:
        print("obrigado por usar o nosso Banco virtual!") 
        break   

# Salva o saldo e o extrato no arquivo antes de sair.
try:
    with open(nome_arquivo, "w") as arquivo:
        json.dump({"saldo": saldo, "extrato": extrato}, arquivo, indent = 4) # Identação para melhor legibiliade.
        print("Dados salvos com sucesso!")
except Exception as e:
    print("Erro ao salvar os dados: {e}.")        