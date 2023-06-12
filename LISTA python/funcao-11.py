# Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida.
import random
day=random.randint(1,31)
month=random.randint(1,12)
monthSelected=''
extenseMonth='janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro'
year=random.randint(1980,2023)
def tranformData(day, month, year):
    print(f'{day}/{month}/{year}')
    print('::TRANSFORMAÇÃO::')
    monthSelected=extenseMonth[month-1]
    print(f'{day} de {monthSelected} de {year}')
tranformData(day,month,year)
