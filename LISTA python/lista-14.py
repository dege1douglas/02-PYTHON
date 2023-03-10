#Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
#"Telefonou para a vítima?"
#"Esteve no local do crime?"
#"Mora perto da vítima?"
#"Devia para a vítima?"
#"Já trabalhou com a vítima?" 
#O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
#Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
#Caso contrário, ele será classificado como "Inocente".
import os
resp=[]
s=0
n=0
resp.append(str(input("Telefonou para a vítima?")))
resp.append(str(input("Esteve no local do crime?")))
resp.append(str(input("Mora perto da vítima?")))
resp.append(str(input("Devia para a vítima?")))
resp.append(str(input("Já trabalhou com a vítima?")))
for i in range(len(resp)):
    if resp[i]=='s' or 'S':
        s=s+1
    else:
        n=n+1
os.system('cls')
if s<2:
    print('Você é INOCENTE!')
elif s==2:
    print('Você é SUSPEITO!')
elif s==3 or s==4:
    print('Você é CÚMPLICE!')
elif s==5:
    print('Você é o ASSASSINO!')
