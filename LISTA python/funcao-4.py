# Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo.
import random
argument=random.randint(-50,50)
def discover(argument):
    print(argument)
    if argument>0:
        print('P')
    elif argument<0:
        print('N')
    else:
        print('NEUTRO')
discover(argument)
