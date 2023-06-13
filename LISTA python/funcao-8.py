#Faça uma função que informe a quantidade de dígitos de um determinado número inteiro informado.
import random
def countDigits(value):
    print(f'{value:^20}')
    print(f':: Número de dígitos :: {len(value)}')
value=str(random.randint(-100000,100000))
countDigits(value)
