#Faça um programa que leia um número indeterminado de valores, correspondentes a notas,
#encerrando a entrada de dados quando for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
#Mostre a quantidade de valores que foram lidos;
#Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
#Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
#Calcule e mostre a soma dos valores;
#Calcule e mostre a média dos valores;
#Calcule e mostre a quantidade de valores acima da média calculada;
#Calcule e mostre a quantidade de valores abaixo de sete;
#Encerre o programa com uma mensagem;
import random
import time
numeros=[]
stop=0
soma=0
media=0
while stop!=-1:
    stop = (int(random.randint(-20,20)))
    if stop!=-1:
        numeros.append(stop)
j = len(numeros)
print('-1 FOI INSERIDO. PROGRAMA FINALIZADO. DADOS GERADOS:::')
print('FORAM GERADOS:',j,' DADOS.')
print('ORDEM CRESCENTE:')
for i in range(j):
    print(f'{[i]} {numeros[i]:>5}', end=' ||| ')
print()
print('ORDEM DECRESCENTE')
for j in range(j,0,-1):
    j-=1
    print(f'{[j]} {numeros[j]:>5}')
for i in range(len(numeros)):
    soma=soma+numeros[i]
    media=media+numeros[i]
media=media/len(numeros)
print('SOMA DOS VALORES:',soma)
print('MÉDIA DOS VALORES:',media)
print('VALORES ACIMA DA MÉDIA:')
for i in range(len(numeros)):
    if numeros[i]>media:
        print(f'{[i]} - {numeros[i]}')
print('VALORES MENORES QUE 7(sete):')
for i in range(len(numeros)):
    if numeros[i]<7:
        print(f'{[i]} - {numeros[i]}')
print('DADOS COMPLETOS.')
print('PROGRAMA IRÁ SE FINALIZAR. :((')
for i in range(5):
    time.sleep(1)
    print('FINALIZANDO',25*i,'%')
print('FINALIZADO.')
