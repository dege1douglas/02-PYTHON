#DOUGLAS DA COSTA GOMES - SALA 2M
#atividade em python
#estádio de futebol - 3 jogos diferentes

#opções de jogos em um estádio 
#variável para o menu ser rotativo
menuz=0

import os
import time

while menuz != 4:
    #menu principal do estádio
    os.system('cls')
    print()
    print("                       ___       ")
    print("   o__        o__     |   |\     ")
    print("  /|          /\      |   |X\    ")
    print("  / > o        <\     |   |XX\   ")
    print()
    print("~ESTÁDIO PROZ DEL GIGANTE DA COLINA~")
    print()
    print("<1> Palestina x Mali")
    print("<2> Etiópia x Burkina Faso")
    print("<3> San Marino x Santa Lúcia")
    print("<4> Para ir EMBORA do ESTÁDIO")
    menuz = int(input("Digite o CÓDIGO do jogo desejado.\n"))

    #ocorrências de jogos
    amarelo = ("CARTÃO AMARELO!")
    vermei = ("CARTÃO VERMELHO! Vai embora mais cedo jogador.")
    impedimento = ("AH não! O bandeirinha estava alerta.\nGOL ANULADO!!!")
    golazo = ("PELO AMOR DE DEUS!!!\nQUE GOLAÇO ABSURDO!!!")
    penalti = ("PENALIDADE MÁXIMA\nQue VACILO em jogador!!!")
    gol = ("GOOOOOOOOOL!!!")
    #inicio tratamento do match-case
    match menuz:
        
        case 1:
            #início do jogo 1
            os.system("cls")
            time1=("PALESTINA")
            time2=("MALI")
            print()
            print("ESTÁDIO PROZ DEL GIGANTE DA COLINA")
            print()
            print("VOCÊ ESCOLHE <PALESTINA x MALI>")
            looP = input("Pressione <ENTER> para começar o jogo:::")
            time.sleep(5) #minuto a minuto do jogo - melhores momentos
            print("          ~INÍCIO DO JOGO~")
            print("          _...----.._              ")
            print("        ,:':::::.     `>.          ")
            print("      ,' |:::::;'     |:::.        ")
            print("     /    `'::'       :::::\        ")
            print("    /         _____     `::;\       ")
            print("   :         /:::::\      `  :     ")
            print("   | ,.     /::SSt::\        |       ")
            print("   |;:::.   `::::::;'        |       ")
            print("   ::::::     `::;'      ,.  ;    ")
            print("    \:::'              ,::::/      ")
            print("     \                 \:::/         ")
            print("      `.     ,:.        :;'         ")
            print("        `-.::::::..  _.''            ") 
            print("           ```----'''                ")
            
            #time casa
            goll=0
            #time fora
            gol1=0

            time.sleep(5)
            print("16' - ",gol,"\nDe TAMER SEYAM\nEle chutou no canto esquerdo com categoria!!!")
            goll=goll+1
            time.sleep(5)
            print("20' - Falta para Mali....\nUma falta que pode trazer perigo ao goleirão Daniel Sappa")
            time.sleep(1)
            print("21' - GOL DE EMPATE DO MALI\n",golazo,"\nUm golaço de Moussa Marega!!!")
            gol1=gol1+1
            time.sleep(5)
            print("38' - MALI FEZ MAIS UM...\nAH não! O bandeirinha estava alerta.\nGOL ANULADO!!!")
            time.sleep(5)
            print("47' - ",penalti,"\nPenâlti para o",time2,"\nGOL da virada do",time2)
            time.sleep(1)
            print("48' -",gol,"")
            gol1=gol1+1
            time.sleep(1)
            print("          ~FIM DO PRIMEIRO TEMPO~")
            time.sleep(5)
            print()
            print("          ~INÍCIO DO SEGUNDO TEMPO~")
            time.sleep(5)
            print("53' - Falta de Nene Dorgeles\nO jogo está esquentando...")
            time.sleep(5)
            print("68' -",gol,"\nIbrahima Koné é o nome da emoção\nUm belo gol para a equipe do",time2)
            time.sleep(5)
            print("70' -",amarelo,"Yaser Hamed deu uma entrada dura no jogador do",time2)
            time.sleep(5)
            print("84' -",gol,"\nQUE EMOÇÃO!\n",time1,"faz mais uma para empartar o jogo novamente.")
            goll=goll+1
            time.sleep(5)
            print("91' -",gol,"\nELES NÃO PARAM!\n",time2,"faz mais um e esse declarou a vitória\nO meia Aliou Dieng marca de cabeça.")
            gol1=gol1+1
            time.sleep(1)
            print("       ~O JUÍZ APITA, FIM DE PAPO!~\n                ~O JOGO ACABOU.~")
            #placar final e retorno ao menu
            print("PLACAR FINAL =====>>>>", time1, goll, "x", gol1, time2)
            if (goll>gol1):
                print("VITÓRIA DO",time1)
            else:
                print("VITÓRIA DO",time2)
            looP = input("FIM DE JOGO!\nAperte <ENTER> para voltar ao MENU do ESTÁDIO!")  


else: #saída do estadio
    os.system("cls")
    print()
    print("Você foi EMBORA do ESTÁDIO!")
    print()
    print("Obrigado por visitá-lo!")