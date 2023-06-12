# Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. Por exemplo: 127 -> 721.
import random
number=random.randint(1000,5000)
def reverseNumber(number):
    number=str(number)
    print(number)
    print('::REVERSO::')
    print(number[::-1])
reverseNumber(number)
