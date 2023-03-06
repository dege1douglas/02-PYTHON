#Faça um Programa que peça a idade e a altura de 5 pessoas,
#armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
idade = []
altura = []
print('Serão impressos os valores de forma contrária ao inserido.')
for i in range(5):
    old=int(input('IDADE: '))
    h=int(input('ALTURA EM CM: '))
    idade.insert(i,old)
    altura.insert(i,h)
print()
for i in range(4,-1,-1):
    print(f'Pessoa -> [{i}]')
    print(f'IDADE: {idade[i]:<4}', end='')
    print(f'ALTURA: {altura[i]:<4}', end='')
    print()
