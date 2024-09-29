from collections import Counter

def analiseTexto(arq1, arq2, cab, vt):
    # Leitura do arquivo de entrada:
    with open(arq1, 'r') as entrada:
        texto = entrada.read()
        texto = [jogo.strip().lower() for jogo in texto.split('*')]
        entrada.close()

    # Conatgem do texto em ordem alfabética e 
    # de acordo com os elementos que mais aparecem:
    dicionario = Counter(sorted(texto)).most_common()

    # Impressão dos dados no arquivo de saída:
    with open(arq2, 'a') as saida:
        saida.write(cab)
        for nome, quantidade in dicionario:
            saida.write(f'{quantidade} | {round((quantidade / vt) * 100, 2):.2f}% | {nome}\n')
        saida.write("\n")
        saida.close()