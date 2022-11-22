#inicio algoritmo
#resolução para equações do segundo grau
import os
#inserção dos valores
print("....................................................................................")
print()
a = float(input("Insira o valor de A: "))
print("....................................................................................")
print()
b= float(input("Insira o valor de B: "))
print("....................................................................................")
print()
c = float(input("Insira o valor de C: "))
delta = float((b**2)-((4*a)*c))

#se delta for negativo
if (delta < 0):
    os.system('cls')
    print("............................O valor de delta:", delta,"............................")
    print()
    print("............................Não existem soluções reais!............................")

#se delta for igual a zero
elif (delta == 0):
    os.system('cls')
    x1=-b/(2*a)
    print ("............................O valor de delta: ", delta,"............................")
    x1 = round(x1, 2)
    print()
    print ("..............Existem duas soluções iguais para a equação:", x1,"..............")

#se delta for positivo e diferente de zero
elif (delta > 0):
    os.system('cls')
    x1 = (-b + delta ** (1 / 2)) / (2 * a)
    x2 = (-b - delta ** (1 / 2)) / (2 * a)

    print("..............Existem duas soluções reais distintas...............")
    print()
    print("..............O valor de delta: ", delta,"..............")
    print()
    print("..............O valor de x1 é: ", x1,"..............")
    print()
    print("..............o valor de x2 é: ", x2,"..............")
    print()
    print("....................................................................................")