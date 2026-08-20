import calculadora_menu

def menu():
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("|1.      Somar       |")
        print("|2.      Subtrair    |")
        print("|3.      Multiplicar |")
        print("|4.      Dividir     |")
        print("|0.      Sair        |")
        print("----------------------")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '0':
            print("Saindo do programa... Obrigado pela visita!")
            break
        elif opcao in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Erro: Por favor, digite apenas números válidos.")
                continue

            if opcao == '1':
                resultado = calculadora_menu.somar(num1, num2)
                print(f"Resultado da Soma: {resultado}")
        else:
            print("Opção inválida! Tente novamente.")
menu ()