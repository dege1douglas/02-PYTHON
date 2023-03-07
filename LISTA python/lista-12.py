#Foram anotadas as idades e alturas de 30 alunos.
#Faça um Programa que determine quantos alunos com mais de 13 anos
#possuem altura inferior à média de altura desses alunos.
import random
altura=[]
idade=[]
cod=[]
media=0
for i in range(30):
    cod.insert(i, int(random.randint(0,30)))
    idade.insert(i, int(random.randint(12,15)))
    altura.insert(i, int(random.randint(150,180)))
    media=media+altura[i]
media=media/30
for i in range(30):
    if idade[i]>13 and altura[i]<media:
        print(f'RESULTADO({[i]})')
        print(f'CODIGO: {cod[i]}')
        print(f'IDADE: {idade[i]}')
        print(f'ALTURA(cm): {altura[i]}')
        print()
