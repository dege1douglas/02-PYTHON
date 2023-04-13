#Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário.
import random
num = int(random.randint(2,10))
num2=num
fatorial=0
total=0
num1=num-1
print(f'Fatorial de {num}:')
while num2>0:
    print(f'{num2}',end='')
    if num2!=1:
        print('.',end='')
    else:
        print('=')
    num2-=1
for i in range(num,1,-1):
    fatorial=num*num1
    total+=fatorial
    num1=num1-1
print('Total:',end='')
print(f'{total}')
