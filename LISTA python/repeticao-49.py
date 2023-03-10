#Faça um programa que mostre os n termos da Série a seguir:
#S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 
n1=1
n2=1
for i in range(25):
    print(f'{[n1]}/{[n2]}',end=' + ')
    n1+=1
    n2+=2
print('n/m.')
