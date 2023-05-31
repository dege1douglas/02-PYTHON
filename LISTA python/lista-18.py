import random
voto_jogador = [0] * 24
percent_jogador = []
voto_total = 0
contador = random.randint(100, 150)
for i in range(contador):
    contador_jogador = random.randint(0, 23)
    if contador_jogador != 0:
        voto_total += 1
        voto_jogador[contador_jogador] += 1
mvp_votos = max(voto_jogador, key=int)
for i in range(24):
    percent_jogador.append(round((voto_jogador[i] / voto_total) * 100))
mvp = voto_jogador.index(mvp_votos)
with open('resultadoPesquisa.txt', 'w') as arquivo:
    arquivo.write('           RESULTADO PESQUISA:\n')
    arquivo.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    arquivo.write(f'            MVP ::: {mvp} - {mvp_votos} votos :::\n')
    arquivo.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    arquivo.write(f'TOTAL VOTOS: {voto_total}\n')
    arquivo.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    arquivo.write('NÚMERO DO JOGADOR   NÚMERO DE VOTOS   PERCENTUAL DE VOTOS\n')
    for i in range(24):
        arquivo.write(f'{i:^16}{voto_jogador[i]:^24}{percent_jogador[i]:>9}%\n')
    arquivo.write('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n')
    arquivo.close()
