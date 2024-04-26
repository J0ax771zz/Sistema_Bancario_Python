menu =("""

====== Bem-Vindo ao nosso Sistema Bancário V1 ======
====== Digite a operação que deseja realizar: ======
            
[d] Depositar
[s] Sacar                        
[e] Extrato
[q] Sair
            
=>""")

# Regras:
#O limite de saque é de R$ 500
# O usuário só pode realizar 3(três) saques diários
# O extrato deve ser mostrado em cada operação

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Você selecionou Depósito")
        deposito = float(input("Digite o valor a ser depositado: "))

        if deposito >0:
            saldo += deposito
            extrato  += f"Deposito: R${deposito: .2f}\n"
            print(f"Seu saldo atualizado é de: R${saldo}")

        else:
            print("Operação inválida, o valor informado é inválido.")
            print (deposito)


    elif opcao == "s":
        print("Você selecionou Saque")
        valor = float(input("Digite o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação cancelada, saldo insuficiente.")
        elif excedeu_limite:
            print("Operaçao cancelada, valor de saque é maior que limite.")
        elif excedeu_saques:
            print("Operação cancelada, o limite de saques diários foi atingido.")

        elif valor >0:
            saldo -= valor
            extrato += f"Saque: R${valor: .2f}\n"
            numero_saques += 1
            print(f"O seu saldo atualizado é de: {saldo}")

        else:
            print("Operação cancelada! O valor informado é inválido")    



    elif opcao == "e":
        print("\n====== EXTRATO BANCÁRIO ======")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R${saldo: .2f}")
        print("==============================")


    elif opcao == "q":
        print("====== Obrigado por usar nosso Sistema Bancário ======")
        break

    else:
        print("Opção inválida, tente novamente") 