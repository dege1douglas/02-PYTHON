# Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos.
import random
def adiction(numb1,numb2,numb3):
    print(f'{numb1}+{numb2}+{numb3}={numb1+numb2+numb3}')
numb1=random.randint(1,10)
numb2=random.randint(1,10)
numb3=random.randint(1,10)
adiction(numb1,numb2,numb3)
