# Faça um programa para imprimir:
#     1
#     1   2
#     1   2   3
#     .....
#     1   2   3   ...  n
# para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima até a n-ésima linha.
import random
count = random.randint(9,9)
def repetidor(count):
    strNumber = ''
    for i in range(count):
        strNumber += f'{str(i)} '
    print(f'{strNumber}')
homelander=0
for i in range(0,count,+1):
    if homelander!=count:
        repetidor(homelander)
    else:
        repetidor(homelander)
        break
    homelander+=1
