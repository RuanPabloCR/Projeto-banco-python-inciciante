situacao = 1
limite = 500
saldo = 0
limite_limite = 0 # ate 3
armazem = []
armazem_Saque = []


while situacao == 1:
    print("""
      Operações:
[D] - Depositar
[S] - Sacar
[E] - extrato
[L] - Sair

""")


    escolha = input("Digite a operação a ser realizada: ")

    if escolha.lower() == "d":
        
        print("Operação de deposito:")
        #while continuar.lower() == "sim":
        deposito_valor = float(input("Qual o valor do depósito:"))
        if deposito_valor > 0:
            saldo = saldo + deposito_valor
            armazem.append(deposito_valor)
            print("Valor depositado com sucesso")
            #print(armazem)
        else:
            print("Operação não concluida!")

    elif escolha.lower() == "s":
        print("Operação de saque")
        if limite_limite < 3:
            valor_saque = float(input("Digite o valor a ser sacado: "))
            if valor_saque > 0 and valor_saque <= 500:
                if saldo >= valor_saque:
                    saldo = saldo - valor_saque
                    armazem_Saque.append(valor_saque)
                    limite_limite = limite_limite + 1
                    print("Saldo sacado com sucesso!")
                    #print(armazem_Saque)
                else:
                    print("Operação de saque fracassada!")
            else:
                ("Operação de saque fracassada!")
        else:
            print("Operação de saque fracassada!")
    elif escolha.lower() == "e":
        print("Operação de extrato")
        print("Depositos: ")
        for valor in armazem:
            print(f"R$ {valor:.2f}")
        print("Saques: ")
        for valor in armazem_Saque:
            print(f"R$ {valor:.2f}")
        print(f"Saldo atual: R$ {saldo:.2f}")
    elif escolha.lower() == "l":
        print("Operações realizadas. programa encerrado")
        situacao = 0

    else:
        print("Comando invalido, tente novamente!")
