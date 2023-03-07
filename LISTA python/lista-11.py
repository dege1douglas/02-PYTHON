#Altere o programa do exercicio 10, intercalando 3 vetores de 10 elementos cada.
import random
vum=[]
vdois=[]
vtres=[]
vquat=[]
for i in range(10):
    vum.insert(i,int(random.randint(0,9)))
    vdois.insert(i,int(random.randint(10,19)))
    vquat.insert(i,int(random.randint(20,29)))
for i in range(10):
    vtres.append(vum[i])
    vtres.append(vdois[i])
    vtres.append(vquat[i])
print(vtres)

