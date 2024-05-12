MENU = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "d":
      deposito=float(input("Digite o valor do deposito: "))
      saldo+=deposito
      extrato+=f"Deposito no valor de: R$ {deposito}\n"

    elif opcao == "s":
      
      if numero_saques>LIMITE_SAQUES:
         print("Numero de saques excedidos!")
      
      else:
        saque=float(input("Digite o valor do saque: "))
        
        if saque>limite:
           print(f"Erro.\nLimite de saque: {limite}")
        
        elif saque>saldo:
          print("Valor indisponivel.")
        
        else:
          saldo-=saque
          extrato+=f"Saque no valor de: R$ {saque}\n"
          print(f"Novo saldo: {saldo}")
          numero_saques+=1
    
    elif opcao == "e":
      print("\n================ EXTRATO ================")
      print("Não foram realizadas movimentações." if not extrato else extrato)
      print(f"\nSaldo: R$ {saldo:.2f}")
      print("==========================================")
    
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")