#Utilize uma lista para resolver o problema a seguir.
#Uma empresa paga seus vendedores com base em comissões. 
#O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. 
#Por exemplo, um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, 
#ou seja, um total de $470. 
#Escreva um programa (usando um array de contadores) que determine quantos vendedores receberam salários nos seguintes intervalos de valores:
#200 - $299
#$300 - $399
#$400 - $499
#$500 - $599
#$600 - $699
#$700 - $799
#$800 - $899
#$900 - $999
#$1000 em diante
#Desafio: Crie ma fórmula para chegar na posição da lista a partir do salário, sem fazer vários ifs aninhados.
import random
salario=[]
vendedor=[]
vendas=[]
x=200
y=299
for i in range(10):
    vendedor.insert(i,(int(random.randint(14763,627463))))
    vendas.insert(i,int(random.randint(0,10000)))
    salario.insert(i,round(200+(vendas[i]*0.09),2))
print('REGISTRO SALARIAL DA SEMANA:')
print('MATRÍCULA      VENDAS BRUTAS       SALÁRIO(R$)')
for i in range(len(vendedor)):
    print(f'{vendedor[i]:<10} {vendas[i]:>10} {salario[i]:>19}')
print()
print('INTERVALOS:')
print()
for i in range(len(vendedor)):
    print(f'${x} - ${y}') 
    for j in range(len(vendedor)):
        if salario[j]<=y and salario[j]>=x:
            print(f'{vendedor[j]:<10}|--|R${salario[j]:>8}|')
    x+=100
    y+=100
