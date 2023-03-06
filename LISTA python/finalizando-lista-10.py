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
#for i in range(10):
    #for k in range(19,1,-2):
        #for h in range(20,0,-2):
            #vtres.insert(h, vum[i])
            #vtres.insert(k, vdois[i])
for i in range(10):
    print(f'{vum[i]}', end=',')
    print(f'{vdois[i]}', end=',')
