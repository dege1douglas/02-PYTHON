#Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero invertido.
numero=str(input('DIGITE VALOR INTEIRO'))
j=len(numero)
l=0
for i in range(j):
    l=j-1
    inv=(numero[l:j])
    print(inv)
    j-=1
