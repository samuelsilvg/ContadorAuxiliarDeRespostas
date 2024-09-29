import funcoes

# Variáveis relevantes:
arqSaida = 'saídas/listaGeral.txt'
quantidade_entrevistados = 17
quantidade_entrevistados_que_jogam_para_aprender_ingles = 16
quantidade_entrevistados_que_usam_aplicativos = 5

# Listando a idade dos participantes:
arqEntrada0 = 'entradas/listaIdades.txt'
cabecalho0 = "IDADES DOS PARTICIPANTES: \n"
funcoes.analiseTexto(arqEntrada0, arqSaida, cabecalho0, quantidade_entrevistados)

# Listando os jogos mais jogados por diversão:
arqEntrada1 = 'entradas/listaJogosJogados.txt'
cabecalho1 = "JOGOS MAIS JOGADOS POR DIVERSAO: \n"
funcoes.analiseTexto(arqEntrada1, arqSaida, cabecalho1, quantidade_entrevistados)

# Listando os jogos mais jogados para aprendizado:
arqEntrada2 = 'entradas/listaJogosAprendizado.txt'
cabecalho2 = "JOGOS MAIS JOGADOS PARA APRENDIZADO: \n"
funcoes.analiseTexto(arqEntrada2, arqSaida, cabecalho2, quantidade_entrevistados_que_jogam_para_aprender_ingles) 

# Listando os gêneros mais jogados:
arqEntrada3 = 'entradas/listaGenerosJogadosOT.txt'
cabecalho3 = "GENEROS MAIS JOGADOS: \n"
funcoes.analiseTexto(arqEntrada3, arqSaida, cabecalho3, quantidade_entrevistados)

# Listando os gêneros mais recomendados:
arqEntrada4 = 'entradas/listaGenerosRecomendados.txt'
cabecalho4 = "GENEROS MAIS RECOMENDADOS: \n"
funcoes.analiseTexto(arqEntrada4, arqSaida, cabecalho4, quantidade_entrevistados)

# Listando os aplicativos usados para aprender inglês:
arqEntrada5 = 'entradas/listaAplicativosAprendizado.txt'
cabecalho5 = "APLICATIVOS USADOS PARA APRENDIZADO: \n"
funcoes.analiseTexto(arqEntrada5, arqSaida, cabecalho5, quantidade_entrevistados_que_usam_aplicativos)
