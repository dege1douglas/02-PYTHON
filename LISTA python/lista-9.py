#Faça um Programa que leia um vetor A com 10 números inteiros,
#calcule e mostre a soma dos quadrados dos elementos do vetor.
import random
a = []
soma=0
print('Será retornado o valor da soma dos quadrados dos valores inseridos.')
for i in range(10):
    a.insert(i, int(random.randint(0,10)))
    a[i] = a[i]*a[i]
    print(f'{a[i]}')
for i in range(10):  
    for k in range(1,10):
        soma=int(soma+a[i]+a[k])
print()
print('SOMA::::')
print('-'*10)
print(soma)
