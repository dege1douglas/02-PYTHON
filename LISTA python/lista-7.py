#Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
numbers=[]
soma=[]
mut=[]
for i in range(0,5):
    number=int(input('Digite os 5 números. '))
    numbers.insert(i,number)
print('Aguarde o resultado(valor efeutado c/ todos outros do vetor, inclusive ele msm):')
for i in range(0,5):
    print()
    print(f'N°={numbers[i]:<5}', end='')
    print()
    for k in range(0,5):
        soma.insert(i,numbers[i]+numbers[k])
        mut.insert(i,numbers[i]*numbers[k])
        print(f'SOMA={soma[i]:<5}', end='')
        print(f'MULTIP.={mut[i]:<5}', end='')
        if k==5:
            print()
