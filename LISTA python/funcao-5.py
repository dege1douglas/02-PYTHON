# Faça um programa com uma função chamada somaImposto. A função possui dois parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em porcentagem e custo, que é o custo de um item antes do imposto. A função “altera” o valor de custo para incluir o imposto sobre vendas.
import random
def somaImposto(taxaImposto, custo):
    print(f'Valor do produto sem imposto:: {custo}')
    print(f'Imposto sobre o produto:: {taxaImposto}%')
    price=round(custo+(custo*(taxaImposto/100)),2)
    print(f'Valor final:: R${price}')
taxaImposto=round(random.uniform(0, 20),1)
custo=round(random.uniform(1, 1500),2)
somaImposto(taxaImposto,custo)
