#Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.

par = []
impar = []
x=0
while x!=20:
    x = x+1
    numb = int(input('Insira números variados.'))
    if numb%2 == 0:
        numb == par.insert(x,numb)
    else:
        numb = impar.insert(x,numb)
x=0
print('PARES')
for x in range(len(par)):
    print(par[x])
print('IMPARES')
for x in range(len(impar)):
    print(impar[x])
