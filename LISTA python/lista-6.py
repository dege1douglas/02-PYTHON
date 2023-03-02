#Faça um Programa que peça as quatro notas de 10 alunos
#, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
import random
import time
notas = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
aluno=[]
med=[]
for x in range(0,4): #inserir aluno e gerar contador
    media=0
    aluno.insert(x, input(f'NOME ALUNO [{x}]')) #nome aluno
    for y in range(0,4):  #contador 2 para correr linhas e colunas da matriz
        notas[x][y] = (int(random.randint(0,10)))
        media = media + notas[x][y]
    media=round(media/4 ,1)
    med.insert(x,media)
print('-='*35) #auto criar linha divisoria
start=input('')
print('ALUNO     ATVD1  ATVD2  ATVD3  ATVD4  MEDIA_F')
for x in range(0,4): #percorrrer a lista e a matriz(colunas)
    time.sleep(1)
    print(f'{aluno[x]:<10}', end='')
    for y in range(0,4): #percorer matriz(linhas)
        print(f'{notas[x][y]:<7}', end='')
    print(f'{med[x]:<7}')
    print()
for x in range(0,4):
    if med[x]>7:
        print('Alunos c/ média > 7')
        print(f'{aluno[x]:^10}', end='')
        print()
