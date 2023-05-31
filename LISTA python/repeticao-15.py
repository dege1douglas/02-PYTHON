# fibonacci
import random
fibo_final=[]
fibo=0
nacci=1
number=random.randint(0,50)
for i in range(number-1):
    fibo_final.append(fibo)
    fibo, nacci = nacci, fibo + nacci
print(f'A SEQUÊNCIA FIBONACCI SERÁ GERADA ATÉ O {len(fibo_final)}º ALGARISMO!')
for i in range(len(fibo_final)):
    print(f'{fibo_final[i]}')
