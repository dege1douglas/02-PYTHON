#sistema de almoxarifado

import os
import random
import time
        
produto = []
quantia = []
codig = []
preco = []
menu1 = 1
menu2 = 0
menu3 = 0
x = 1
contador = 1

while (menu1!=5):
    x=1
    os.system('cls')
    print(" __ _____ _  _     __  ")
    print("|_ (_  | / \/ \| ||_   ") 
    print("|____) | \_/\_X|_||__  ")
    print()
    print()
    print("SISTEMA DE ESTOQUE")
    print(" < 1 > CADASTRAR PRODUTO")
    print(" < 2 > CONSULTAR ESTOQUE")
    print(" < 3 > ADICIONAR ESTOQUE PRODUTO")
    print(" < 5 > FINALIZAR.")
    menu1 = int(input('DIGITE SUA ESCOLHA '))
    
    match(menu1):
        case 1:
            while(x!=2):
                print("CADASTRAR PRODUTO NOVO")
                print()
                produto.append((str(input("INSIRA O NOME DO PRODUTO "))))
                quantia.append((int(input("INSIRA A QUANTIDADE "))))
                codig.append((int(input("INSIRA O CÓDIGO DO PRODUTO "))))
                
                for contador in range(0,5):
                    preco.insert(contador,(int(random.randint(1, 50))))
                os.system('cls')

                print("PRODUTO CADASTRADO COM SUCESSO!")
                print("DESEJA CADASTRAR OUTRO PRODUTO?")
                x = int(input("1 para <SIM> -- 2 para <NÃO>."))
        case 2:
            print("VEJA SE HÁ O PRODUTO NO ESTOQUE.")
            print("< 1 > CONSULTA INDIVIDUAL DE PRODUTOS.")
            print("< 2 > CONSULTAR ESTOQUE COMPLETO.")
            menu2 = int(input())
            match(menu2):

                case 1:
                    os.system('cls')
                    print("CONSULTA INDIVIDUAL DE PRODUTOS")
                    c = int(input("DIGITE o CÓDIGO DO PRODUTO. "))
                    if (c == codig[0]):
                        print(codig[0]," - ",produto[0]," - R$",preco[0],",00 - ",quantia[0]," unidades.")
                    elif (c == codig[1]):
                        print(codig[1]," - ",produto[1]," - R$",preco[1],",00 - ",quantia[1]," unidades.")   
                    elif (c == codig[2]):
                        print(codig[2]," - ",produto[2]," - R$",preco[2],",00 - ",quantia[2]," unidades.")
                    elif (c == codig[3]):
                        print(codig[3]," - ",produto[3]," - R$",preco[3],",00 - ",quantia[3]," unidades.")
                    elif (c == codig[4]):
                        print(codig[4]," - ",produto[4]," - R$",preco[4],",00 - ",quantia[4]," unidades.")
                    elif (c == codig[5]):
                        print(codig[5]," - ",produto[5]," - R$",preco[5],",00 - ",quantia[5]," unidades.")
                        lop = input()
                        
                case 2:
                    print("ESTOQUE COMPLETO.")
                    print()
                   
                    contador=0
                    for contador in range(0,len(codig)):
                        print()
                        if (codig[contador]==None):
                            print(contador,' - vazio    -    vazio    -    R$00,00    -    0 unidades.')
                        print(contador," - ",codig[contador]," - ",produto[contador]," - R$",preco[contador],",00 - ",quantia[contador]," unidades.")
                    lop = (input())

        case 3:
            c=1
            x=1
            while (x!=2):
                print("ADICIONAR PRODUTOS AO ESTOQUE")
                c = int(input("DIGITE O CÓDIGO DO PRODUTO. "))
                for contador in range (0,5):
                    if (c == codig[0]):
                        q = int(input("DIGITE A QUANTIA À ADICIONAR "))
                        quantia[0]=quantia[0]+q
                    if (c == codig[1]):
                        q = int(input("DIGITE A QUANTIA À ADICIONAR "))
                        quantia[1]=quantia[1]+q
                    if (c == codig[2]):
                        q = int(input("DIGITE A QUANTIA À ADICIONAR "))
                        quantia[2]=quantia[2]+q
                    if (c == codig[3]):
                        q = int(input("DIGITE A QUANTIA À ADICIONAR "))
                        quantia[3]=quantia[3]+q
                    if (c == codig[4]):
                        q = int(input("DIGITE A QUANTIA À ADICIONAR "))
                        quantia[4]=quantia[4]+q
                    if (c == codig[5]):
                        q = int(input("DIGITE A QUANTIA À ADICIONAR "))
                        quantia[5]=quantia[5]+q
                        

                print("ESTOQUE ATUALIZADO COM SUCESSO!")
                print("DESEJA ADICIONAR OUTRO PRODUTO?")
                x = int(input("1 para <SIM> -- 2 para <NÃO>."))