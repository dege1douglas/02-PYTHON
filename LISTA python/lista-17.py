#Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
#O resultado do atleta será determinado pela média dos cinco valores restantes.
#Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe o nome,
#os saltos e a média dos saltos. O programa deve ser encerrado quando não for informado o nome do atleta.
import random
salto1=[]
salto2=[]
salto3=[]
salto4=[]
salto5=[]
atleta=[]
med=[]
media=0
x=0
while x!=1:
    atleta.append(str(input('Nome do atleta.\n')))
    for i in range(len(atleta)):
        if atleta[i]=='':
            x+=1
        elif atleta[i]!='':
            salto1.append(round(random.uniform(3.1,8.9),2))
            salto2.append(round(random.uniform(3.1,8.9),2))
            salto3.append(round(random.uniform(3.1,8.9),2))
            salto4.append(round(random.uniform(3.1,8.9),2))
            salto5.append(round(random.uniform(3.1,8.9),2))
            media=salto1[i]+salto2[i]+salto3[i]+salto4[i]+salto5[i]
            print(f'Atleta:{atleta[i]:^10}\n1º salto:{salto1[i]:>6}\n2º salto:{salto2[i]:>6}\n3º salto:{salto3[i]:>6}\n4º salto:{salto4[i]:>6}\n5º salto:{salto5[i]:>6}')
            print()
    med.append(round(media/5,2))
else:
    for i in range(len(atleta)):
        if atleta[i]!='':
            print(f'Resultado Final:\nAtleta:{atleta[i]:^10}\nSaltos: {salto1[i]} - {salto2[i]} - {salto3[i]} - {salto4[i]} - {salto5[i]}\nMédia dos saltos: {med[i]:>1}')
            print()
    print('Programa finalizado.')
