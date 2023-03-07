#Faça um programa que receba a temperatura média de cada mês do ano e
#armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual,
#e em que mês elas ocorreram (mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro,
import random
mes=['janeiro','fervereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
tempm=[]
media=0.0
for i in range(12):
    tempm.insert(i, int(random.randint(19.0,30.0)))
    media=media+tempm[i]
media= round(media/12,1)
print('MÉDIA ANUAL :::> ',media)
print()
c=0
for i in range(12):
    c+=1
    if tempm[i]>media:
        print(f'{c:<3} - {mes[i]:^12} - {tempm[i]:<5}')
