# Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos valores de entrada todas as vezes que desejar.
import time,random
def converter(hour):
    global info
    global newHour
    meridianSelected=''
    if hour>12:
        newHour=hour-12
        info=1
    elif hour==12:
        newHour=hour
        info=1
    else:
        newHour=hour
        info=0
def resultHour(newHour,minutes,info):
    meridian=['A.M.','P.M.']
    print(f':: HORAS CONVERTIDAS :: {newHour} : {minutes} {meridian[info]}')
while True:
    hour=random.randint(0,23)
    minutes=random.randint(0,59)
    for i in range(0,3):
        time.sleep(1)
        print('.')
    time.sleep(1)
    print(f':: HORAS INFORMADAS :: {hour} : {minutes}')
    time.sleep(0)
    converter(hour)
    resultHour(newHour,minutes,info)
    loop=int(input(':: CONVERTER MAIS? (1)SIM | (2)NÃO :: '))
    if loop==2:
        break
