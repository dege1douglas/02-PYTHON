menu=0

while menu != 5:
    print()
    print("ESCOLHA NA LISTA A OPERAÇÃO DESEJADA:")
    print()
    print("<1> - ADIÇÃO")
    print("<2> - SUBTRAÇÃO")
    print("<3> - DIVISÃO")
    print("<4> - MULTIPLICAÇÃO")
    print("<5> - SAIR DO PROGRAMA")
    menu = int(input("Digite sua escolha.\n"))

    match menu:
        case 1:
            print()
            print("~ADIÇÃO~")
            print()
            a = int(input("Digite o primeiro valor:\n"))
            print()
            b = int(input("Digite o próximo valor:\n"))
            soma = int(a+b)
            print(soma,"é o valor da soma.")
            print()
            looP = input("Pressione <ENTER> para voltar ao menu.")
        case 2:
            print()
            print("~SUBTRAÇÃO~")
            print()
            a = int(input("Digite o primeiro valor:\n"))
            print()
            b = int(input("Digite o próximo valor:\n"))
            subt = int(a-b)
            print(subt,"é o valor da subrtração.")
            print()
            looP = input("Pressione <ENTER> para voltar ao menu.")
     
        #inicio tratamento do caso divisão
        case 3:
            print()
            print("~DIVISÃO~")
            print()
            a = int(input("Digite o primeiro valor:\n"))
            print()
            b = int(input("Digite o próximo valor:\n"))
            diviS = int(a/b)
            print(diviS,"é o valor da divisão.")
            print()
            looP = input("Pressione <ENTER> para voltar ao menu.")

        #inicio do tratamento do caso mutliplicação
        case 4:
            print()
            print("~MULTIPLICAÇÃO~")
            print()
            a = int(input("Digite o primeiro valor:\n"))
            print()
            b = int(input("Digite o próximo valor:\n"))
            multP = int(a*b)
            print(multP,"é o valor da multiplicação.")
            print()
            looP = input("Pressione <ENTER> para voltar ao menu.")
else: 
    print("O programa foi executado com sucesso!")