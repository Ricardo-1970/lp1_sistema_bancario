import datetime

saldo = 1000.0 #Saldo inicial.
extrato = [] #Lista para armazenar as transações.

def consultar_saldo(): # função adicionada ao código para torná - lo funcional.
    """Exibe o saldo atual. """
    global saldo, extrato
    agora = datetime.datetime.now() # uso da mesma chave - "agora" - .
    extrato.append({"data_hora": agora,"tipo": "Consulta Saldo","valor": saldo}) # dicionário inserido.
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
        extrato.append({"data_hora": agora,"tipo": "Saque", "valor": valor_saque})
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
    extrato.append({"data_hora": agora,"tipo": "Depósito", "valor": valor_deposito})
    print(f"Depósito de R$ {valor_deposito:.2f} realizado com sucesso.") 
    print(f"Seu novo saldo é: R$ {saldo:.2f}")

def exibir_extrato():
    """Exibe o extrato bancário"""
    global extrato
    if not extrato:
        print("Não foram realizadas transações")
    else:
        print("\n --- Extrato Bancário ---")
        for transacao in extrato:
            data_hora = transacao["data_hora"].strftime("%d/%m/%Y - %H:%M:%S")
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
    print("4 - Exibir Extrato") # opção para exibir extrato.
    print("5 - Sair")

    while True:
        try:
            opcao_str = input("Digite a opção desejada: ")
            opcao = int(opcao_str)
            if 1 <= opcao <= 5: # modifiquei para incluir a opção 5.
                 break 
            else:
                print("Opção inválida. Por favor. Digite um número entre 1 e 5.")
        except ValueError:
            print("Opção inválida. Por favor, digite um número inteiro.")

    if opcao == 1:
        consultar_saldo()
    elif opcao == 2:
        depositar()
    elif opcao == 3:
        sacar()
    elif opcao == 4: # Nova condição para exibir extrato.
        exibir_extrato()   
    elif opcao == 5:
        print("obrigado por usar o nosso Banco virtual!") 
        break   