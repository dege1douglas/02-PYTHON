#Faça um Programa que leia dois vetores com 10 elementos cada.
#Gere um terceiro vetor de 20 elementos,
#cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
import random
vum=[]
vdois=[]
vtres=[]
for i in range(10):
    vum.insert(i,int(random.randint(0,9)))
    vdois.insert(i,int(random.randint(10,19)))
for i in range(10):
    vtres.append(vum[i])
    vtres.append(vdois[i])
print(vtres)
