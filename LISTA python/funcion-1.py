# Faça um programa para imprimir:
#     1
#     2   2
#     3   3   3
#     .....
#     n   n   n   n   n   n  ... n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
import random
count = random.randint(1,9)
def repetidor(count):
    strNumber = ''
    for i in range(count):
        strNumber += f'{str(count)} '
    print(f'{strNumber}')
homelander=1
for i in range(0,count,+1):
    if homelander!=count:
        repetidor(homelander)
    else:
        repetidor(homelander)
        break
    homelander+=1
