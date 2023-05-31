# fibonacci até que seja > 500
fibo_final=[]
fibo=0
nacci=1
for i in range(20):
    fibo_final.append(fibo)
    fibo, nacci = nacci, fibo + nacci
print('::A sequência fibonacci até que seja maior que 500 é::')
for i in range(len(fibo_final)):
    if fibo_final[i]<500:
        print(f'{fibo_final[i]:^50}')
    else:
        print(f'{fibo_final[i]:^50}')
        break
