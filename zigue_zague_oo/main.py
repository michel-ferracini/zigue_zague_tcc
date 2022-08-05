import ziguezague

if __name__ == "__main__":
    #  CONFIGURAÇÕES INICIAIS
    zz = ziguezague.ZigueZague()  # Instancia a classe ZigueZague().

    print(f'\nExemplo de retorno da lista da próxima jogada para posição 1 e maior índice 2: {zz.listaProximaJogada(1, 2)}')

    print('\nTodos os possíveis caminhos no tabuleiro 4 X 3:\n')
    for caminho in zz.totalCaminhosTeste():
        print(caminho, end=' ')

    print(f'\n\nTotal de caminhos distintos no tabuleiro 4 X 3: {len(zz.totalCaminhosTeste())}')

    configuracoes = zz.produtoFiltrado()

    print(f'Primeira possível configuração para o lançamento de três dados: {configuracoes[0]}')
    print(f'Total de configurações distintas para os três dados: {len(configuracoes)}')

    resultados_expressoes = zz.resultadosExpressoes(configuracoes)
    cardinalidade = len(resultados_expressoes)
    resultados_expressoes.sort()  # Ordena a lista de resultados do menor para o maior.

    print(f'\nCardinalidade do espaço amostral: {cardinalidade}')
    print(f'Menor resultado: {resultados_expressoes[0]}')
    print(f'Maior resultado: {resultados_expressoes[cardinalidade - 1]}')

    evento = 7  # Altere este valor (um número inteiro de 1 a 10) para visualizar a
    # cardinalidade de cada evento.

    print(f'Cardinalidade do evento {evento}: {zz.cardinalidade(evento, configuracoes)}')
    print(f'Probabilidade do evento {evento}: {round(zz.probabilidade(evento, configuracoes), 6)}')

    linha = 4  # Altere esta linha para um valor entre 1 e 11.
    coluna = 6  # Altere esta linha para um valor entre 1 e 9.

    tab_proba = zz.tabProba(configuracoes)

    casa = tab_proba[linha - 1][coluna - 1]  # (lin, col, valor, probabilidade)
    valor = casa[2]
    proba = casa[3]

    print('\nTabuleiro de probabilidades:'
          f'\nCasa da linha {linha} e coluna {coluna} - Valor: {valor}, '
          f'Probabilidade: {round(proba, 6)}')

    mapa_tabuleiro = zz.mapaTabuleiro(tab_proba)

    print('\nPrimeiro caminho do mapa do tabuleiro:')
    for item in mapa_tabuleiro[0][0]:
        print(item)
    print(f'Probabilidade do primeiro caminho: {mapa_tabuleiro[0][1]}')

    distintas_probas = zz.distintasProbas(mapa_tabuleiro)

    print(f'\nTotal de caminhos com distintas probabilidades: {len(distintas_probas)}')

    valores = zz.valoresExtremos(distintas_probas)
    menor_proba = valores[0]
    maior_proba = valores[1]

    print(f'\nMenor probabilidade (dos caminhos): {menor_proba}')
    print(f'Maior probabilidade (dos caminhos): {maior_proba}')

    total_menor = 0  # Variável para armazenar o total de caminhos com menor probabilidade.
    total_maior = 0  # Variável para armazenar o total de caminhos com maior probabilidade.

    # No laço abaixo, cada item é um par da forma (caminho, probabilidade do caminho).
    for item in mapa_tabuleiro:  # mapa_tabuleiro foi obtida como retorno da função mapaTabuleiro() anteriormente.
        if item[1] == menor_proba:
            total_menor += 1
        if item[1] == maior_proba:
            total_maior += 1

    print(f'\nTotal de caminhos que possuem probabilidade mínima: {total_menor}.')
    print(f'Total de caminhos que possuem probabilidade máxima: {total_maior}.')

    sub_mapa_maior_proba = []  # Lista que recebe os caminhos de maior probabilidade
    for item in mapa_tabuleiro:  # "item" é guardado na lista quando sua probabilidade
        if item[1] == maior_proba:  # é a maior.
            sub_mapa_maior_proba.append(item)

    sub_mapa_menor_proba = []  # Lista que recebe os caminhos de menor probabilidade
    for item in mapa_tabuleiro:  # "item" é guardado na lista quando sua probabilidade
        if item[1] == menor_proba:  # é a menor.
            sub_mapa_menor_proba.append(item)

    # Percorre a lista de caminhos de maior probabilidade
    for item in sub_mapa_maior_proba:
        zz.imprimeCaminho(item, 20, 'green')

    # Percorre a lista de caminhos de menor probabilidade
    for item in sub_mapa_menor_proba:
        zz.imprimeCaminho(item, 20, 'red')

    print('\nCaminhos mais prováveis: em verde')
    print('Caminhos menos prováveis: em vermelho.')

    zz.configGraficos()

    submapa_inferior = zz.mapaFaixaProbas(mapa_tabuleiro, distintas_probas, 0, 999)
    submapa_superior = zz.mapaFaixaProbas(mapa_tabuleiro, distintas_probas, 22076, 23076)

    # Percorre a lista de caminhos de maior probabilidade e imprime cada um.
    for caminho in submapa_superior:
        zz.imprimeCaminho(caminho, 1, 'green')

    # Percorre a lista de caminhos de menor probabilidade e imprime cada um.
    for caminho in submapa_inferior:
        zz.imprimeCaminho(caminho, 1, 'red')

    print('\tCaminhos mais prováveis: em verde')
    print('\tCaminhos menos prováveis: em vermelho.')

    zz.configGraficos()

