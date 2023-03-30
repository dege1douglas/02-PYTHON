#Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
#O resultado do atleta será determinado pela média dos cinco valores restantes. 
#Você deve fazer um programa que receba o nome e as cinco distâncias 
#alcançadas pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. 
#O programa deve ser encerrado quando não for informado o nome do atleta. 
import random
salto1=[]
salto2=[]
salto3=[]
salto4=[]
salto5=[]
atleta=[]
media=0
x=0
j=1
for i in range(j):
    atleta.append(str(input('Nome do atleta.\n')))
    if atleta[x]=='':
        x=1
        print('Não foi informando um nome válido. Programa finalizado.')
        break
    elif atleta[i]!='':
        j+=1
        salto1.append(round(random.uniform(3.1,8.9),2))
        salto2.append(round(random.uniform(3.1,8.9),2))
        salto3.append(round(random.uniform(3.1,8.9),2))
        salto4.append(round(random.uniform(3.1,8.9),2))
        salto5.append(round(random.uniform(3.1,8.9),2))
        media=salto1[i]+salto2[i]+salto3[i]+salto4[i]+salto5[i]
    media=round(media/5,2)
    print(f'{salto1[i]}\n{salto2[i]}\n{salto3[i]}\n{salto4[i]}\n{salto5[i]}\n{media}')
    
