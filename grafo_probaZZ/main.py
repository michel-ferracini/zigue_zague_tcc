if __name__ == "__main__":

    def listaProximaJogada(posicaoAtual, colunaMAX):
        if posicaoAtual == 0:
            return [0, 1]
        elif posicaoAtual == colunaMAX:
            return [colunaMAX - 1, colunaMAX]
        elif 0 < posicaoAtual < colunaMAX:
            return [posicaoAtual - 1, posicaoAtual, posicaoAtual + 1]
        else:
            return []


    print(f'Exemplo de retorno para posição 1 e maior índice 2: {listaProximaJogada(1, 2)}')


    def totalCaminhosTeste():
        # Modelo do tabuleiro de teste:
        tab = [
            [7, 5, 6],  # linha 1 = tab[0] - Início do jogo
            [2, 8, 1],  # linha 2 = tab[1]
            [7, 3, 2],  # linha 3 = tab[2]
            [5, 8, 7],  # linha 4 = tab[3] - Fim do jogo
        ]
        colunaMAX = 2  # Maior índice das colunas do tabuleiro.
        caminhos = []  # Lista para receber os caminhos.
        # Laços para construir todos os possíveis caminhos no tabuleiro 4 X 3:
        for p1 in [0, 1, 2]:  # p1 é a posição na linha 1, p2 é a posição na linha 2, etc.
            for p2 in listaProximaJogada(p1, colunaMAX):
                for p3 in listaProximaJogada(p2, colunaMAX):
                    for p4 in listaProximaJogada(p3, colunaMAX):
                        caminhos.append([tab[0][p1], tab[1][p2], tab[2][p3], tab[3][p4]])
        return caminhos


    print('Todos os possíveis caminhos no tabuleiro 4 X 3:\n')
    for caminho in totalCaminhosTeste():
        print(caminho, end=' ')

    print(f'\n\nTotal de caminhos distintos no tabuleiro 4 X 3: {len(totalCaminhosTeste())}')

    from itertools import permutations, product


    def produtoFiltrado():
        D = [1, 2, 3, 4, 5, 6]  # A lista D representa cada um dos três dados usados no jogo.
        produto = list(product(D, D, D))  # Produto cartesiano: D X D X D.
        produto_filtrado = []  # Lista para receber todos os distintos resultados da lista "produto".
        while (produto):  # Percorre a lista "produto" enquanto ela não for vazia.
            produto_filtrado.append(produto[0])  # Guarda o primeiro produto na lista.
            # Lista de todas as permutações de produto[0]:
            permutacoes = list(permutations([produto[0][0], produto[0][1], produto[0][2]]))
            # Remove todas as permutações de "produto[0]"
            # (inclusive remove "produto[0]", diminuindo um elemento da lista "produto").
            for p in permutacoes:
                if p in produto:
                    produto.remove(p)
        return produto_filtrado


    configuracoes_dados = produtoFiltrado()

    print(f'Primeira possível configuração para o lançamento de três dados: {configuracoes_dados[0]}\n')

    print(f'Total de configurações distintas para os três dados: {len(configuracoes_dados)}')


    def resultadosExpressoes(configuracoes_dados):
        # Lista que recebe todos os possíveis resultados de todas as expressões
        # numéricas obtidas com as coordenadas de cada terna obtida no experimento aleatório:
        resultados = []
        # Laço que percorre cada terna obtida no experimento aleatório:
        for p in configuracoes_dados:
            if p[0] == p[1] and p[1] == p[2]:  # Se a = b = c, na terna (a,b,c), então adicionamos
                # as expressões abaixo à lista "resultados":
                resultados.append(p[0] + p[1] + p[2])  # a + b + c
                resultados.append(p[0] + p[1] - p[2])  # a + b - c
                resultados.append(p[0] - p[1] - p[2])  # a - b - c
            elif p[0] == p[1]:  # Se a = b, adicionamos:
                resultados.append(p[0] + p[1] + p[2])  # a + b + c
                resultados.append(p[0] + p[1] - p[2])  # a + b - c
                resultados.append(p[0] - p[1] + p[2])  # a - b + c
                resultados.append(p[0] - p[1] - p[2])  # a - b - c
                resultados.append(p[2] - p[0] - p[1])  # c - a - b
            elif p[1] == p[2]:  # Se b = c, adicionamos:
                resultados.append(p[0] + p[1] + p[2])  # a + b + c
                resultados.append(p[0] + p[1] - p[2])  # a + b - c
                resultados.append(p[0] - p[1] - p[2])  # a - b - c
                resultados.append(p[1] - p[0] + p[2])  # b - a + c
                resultados.append(p[1] - p[0] - p[2])  # b - a - c
            elif p[0] == p[2]:  # Se a = c, adicionamos:
                resultados.append(p[0] + p[1] + p[2])  # a + b + c
                resultados.append(p[0] + p[1] - p[2])  # a + b - c
                resultados.append(p[0] - p[1] + p[2])  # a - b + c
                resultados.append(p[0] - p[1] - p[2])  # a - b - c
                resultados.append(p[1] - p[0] - p[2])  # b - a - c
            else:  # Se a != b e b != c e a != c, adicionamos:
                resultados.append(p[0] + p[1] + p[2])  # a + b + c
                resultados.append(p[0] + p[1] - p[2])  # a + b - c
                resultados.append(p[0] - p[1] + p[2])  # a - b + c
                resultados.append(p[0] - p[1] - p[2])  # a - b - c
                resultados.append(p[1] - p[0] + p[2])  # b - a + c
                resultados.append(p[1] - p[0] - p[2])  # b - a - c
                resultados.append(p[2] - p[0] - p[1])  # c - a - b
        return resultados


    resultados_expressoes = resultadosExpressoes(configuracoes_dados)
    resultados_expressoes.sort()  # Ordena a lista de resultados do menor para o maior.

    print(f'Cardinalidade do espaço amostral: {len(resultados_expressoes)}')

    print(f'Menor resultado: {resultados_expressoes[0]}')
    print(f'Maior resultado: {resultados_expressoes[len(resultados_expressoes) - 1]}')


    def cardinalidade(evento, resultados_expressoes):
        cardinalidade = 0
        for r in resultados_expressoes:
            if r == evento:
                cardinalidade += 1
        return cardinalidade


    evento = 7  # Altere este valor (um número inteiro de 1 a 10) para visualizar a
    # cardinalidade de cada evento.

    print(f'Cardinalidade do evento {evento}: {cardinalidade(evento, resultados_expressoes)}')


    def probabilidade(evento, resultados_expressoes):
        return cardinalidade(evento, resultados_expressoes) / len(resultados_expressoes)


    evento = 7  # Altere este valor (um número inteiro de 1 a 10) para visualizar a
    # probabilidade de cada evento.

    print(f'Probabilidade do evento {evento}: {round(probabilidade(evento, resultados_expressoes), 6)}')


    def tabProba(resultados_expressoes):
        # Modelo do tabuleiro:
        tab = [
            [7, 5, 6, 9, 4, 2, 8, 1, 3],  # linha 1  = tab[0]  - Início do jogo
            [2, 8, 1, 8, 10, 7, 9, 4, 5],  # linha 2  = tab[1]
            [7, 3, 2, 1, 5, 4, 5, 7, 3],  # linha 3  = tab[2]
            [5, 8, 7, 2, 8, 7, 6, 9, 8],  # linha 4  = tab[3]
            [7, 3, 2, 1, 5, 4, 5, 7, 3],  # linha 5  = tab[4]
            [2, 4, 8, 5, 9, 7, 6, 8, 5],  # linha 6  = tab[5]
            [8, 7, 3, 6, 4, 1, 2, 5, 1],  # linha 7  = tab[6]
            [6, 2, 5, 7, 8, 7, 6, 4, 3],  # linha 8  = tab[7]
            [8, 7, 6, 3, 5, 4, 9, 2, 7],  # linha 9  = tab[8]
            [5, 4, 3, 8, 9, 1, 2, 5, 4],  # linha 10 = tab[9]
            [2, 9, 7, 4, 6, 8, 7, 5, 9],  # linha 11 = tab[10] - Fim do jogo
        ]
        # Tabuleiro de probabilidades: modelo vazio do tabuleiro, para receber as
        # probabilidades de cada casa.
        tab_proba = [
            [],  # linha 1  = tab[0]  - Início do jogo
            [],  # linha 2  = tab[1]
            [],  # linha 3  = tab[2]
            [],  # linha 4  = tab[3]
            [],  # linha 5  = tab[4]
            [],  # linha 6  = tab[5]
            [],  # linha 7  = tab[6]
            [],  # linha 8  = tab[7]
            [],  # linha 9  = tab[8]
            [],  # linha 10 = tab[9]
            [],  # linha 11 = tab[10] - Fim do jogo
        ]
        for lin in range(len(tab)):  # Percorre as linhas no tabuleiro.
            for col in range(len(tab[0])):  # Percorre as colunas em cada linha.
                tab_proba[lin].append([lin, col, tab[lin][col], probabilidade(tab[lin][col], resultados_expressoes)])
                # Na linha acima, é calculada e adicionada a quadra (lin, col, valor, probabilidade)
                # ao tabuleiro de probabilidades, onde lin indica a linha e col a coluna.
        return tab_proba


    linha = 4  # Altere esta linha para um valor entre 1 e 11.
    coluna = 6  # Altere esta linha para um valor entre 1 e 9.

    tab_proba = tabProba(resultados_expressoes)

    casa = tab_proba[linha - 1][coluna - 1]  # (lin, col, valor, probabilidade)
    valor = casa[2]
    proba = casa[3]

    print(f'Casa da linha {linha} e coluna {coluna} - Valor: {valor}, Probabilidade: {round(proba, 6)}')


    # Função que recebe um caminho e retorna sua probabilidade.
    def probaCaminho(caminho):
        produto = 1  # variável que será retornada com a probabilidade do caminho.
        for item in caminho:
            produto *= item[3]
        return produto


    # Função que calcula as probabilidades de cada caminho e retorna uma lista com
    # os pares (caminho, probabilidade do caminho).
    def mapaTabuleiro(tab_proba):
        colunaMAX = 8  # Guarda o maior índice de coluna do tabuleiro.
        mapa = []  # Lista vazia para receber os pares (caminho, probabilidade do caminho).
        # Determina todos os possíveis caminhos no tabuleiro 11 X 9:
        for p1 in [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # p1 é a posição na linha 1,
            for p2 in listaProximaJogada(p1, colunaMAX):  # p2 é a posição na linha 2, etc.
                for p3 in listaProximaJogada(p2, colunaMAX):
                    for p4 in listaProximaJogada(p3, colunaMAX):
                        for p5 in listaProximaJogada(p4, colunaMAX):
                            for p6 in listaProximaJogada(p5, colunaMAX):
                                for p7 in listaProximaJogada(p6, colunaMAX):
                                    for p8 in listaProximaJogada(p7, colunaMAX):
                                        for p9 in listaProximaJogada(p8, colunaMAX):
                                            for p10 in listaProximaJogada(p9, colunaMAX):
                                                for p11 in listaProximaJogada(p10, colunaMAX):
                                                    caminho = [
                                                        tab_proba[0][p1], tab_proba[1][p2],
                                                        tab_proba[2][p3], tab_proba[3][p4],
                                                        tab_proba[4][p5], tab_proba[5][p6],
                                                        tab_proba[6][p7], tab_proba[7][p8],
                                                        tab_proba[8][p9], tab_proba[9][p10],
                                                        tab_proba[10][p11]
                                                    ]
                                                    proba = probaCaminho(caminho)
                                                    mapa.append((caminho, proba))
        return mapa


    mapa_tabuleiro = mapaTabuleiro(tab_proba)

    print('Primeiro caminho:')
    for item in mapa_tabuleiro[0][0]:
        print(item)
    print(f'\nProbabilidade do primeiro caminho: {mapa_tabuleiro[0][1]}')


    # Função que retorna uma lista com todos os diferentes valores de probabilidades
    # encontrados no mapeamento do tabuleiro.
    def distintasProbas(mapa_tabuleiro):
        distintas_probas = []  # Guarda os distintos valores de probabilidades dos caminhos.
        for caminho in mapa_tabuleiro:
            if caminho[1] not in distintas_probas:
                distintas_probas.append(caminho[1])
        return distintas_probas


    distintas_probas = distintasProbas(mapa_tabuleiro)

    print(f'Total de caminhos com distintas probabilidades: {len(distintas_probas)}')


    def valoresExtremos(distintas_probas):
        tam = len(distintas_probas)
        distintas_probas.sort()  # Ordena distintas_probas do menor para o maior elemento.
        menor_proba = distintas_probas[0]
        maior_proba = distintas_probas[tam - 1]
        return (menor_proba, maior_proba)


    valores_extremos = valoresExtremos(distintas_probas)
    menor_proba = valores_extremos[0]
    maior_proba = valores_extremos[1]

    print(f'Menor probabilidade (dos caminhos): {menor_proba}')
    print(f'Maior probabilidade (dos caminhos): {maior_proba}')

    total_menor = 0  # Variável para armazenar o total de caminhos com menor probabilidade.
    total_maior = 0  # Variável para armazenar o total de caminhos com maior probabilidade.

    # No laço abaixo, cada item é um par da forma (caminho, probabilidade do caminho).
    for item in mapa_tabuleiro:  # mapa_tabuleiro foi obtida como retorno da função mapaTabuleiro() anteriormente.
        if item[1] == menor_proba:
            total_menor += 1
        if item[1] == maior_proba:
            total_maior += 1

    print(f'Total de caminhos que possuem probabilidade mínima: {total_menor}.')
    print(f'Total de caminhos que possuem probabilidade máxima: {total_maior}.')

    from matplotlib import pyplot as plt
    import random as rd


    # Função que retorna um número aleatório entre 0.15 e 0.85. Esse valor será utilizado como incremento para as
    # coordenadas dos pontos que serão impressos no infográfico dos caminhos.
    def valorAleatorio():
        acrescimo = rd.random()
        if acrescimo > 0.85:
            acrescimo = 0.85
        elif acrescimo < 0.15:
            acrescimo = 0.15
        return acrescimo


    # Função que imprime todos o caminho em qualquer par de um submapa do mapeamento do tabuleiro.
    def imprimeCaminho(par, tamanho, cor):
        coord_lin = []
        coord_col = []
        caminho = par[0]  # Caminho no mapeamento
        for posicao in caminho:  # Para cada posição ocupada no tabuleiro
            coord_lin.append(posicao[0] + valorAleatorio())  # Grava linha + acréscimo em coord_lin
            coord_col.append(posicao[1] + valorAleatorio())  # Grava coluna + acréscimo em coord_col
        plt.scatter(coord_col, coord_lin, color=cor, marker='s', s=tamanho)  # Imprime os pontos no gráfico


    # Configurações do infográfico.
    def configGraficos():
        plt.xlabel("Colunas", fontsize=14)
        plt.ylabel("Linhas", fontsize=14)
        plt.xticks(range(0, 10))
        plt.yticks(range(0, 12))
        plt.grid(color='black', linestyle='solid', linewidth=0.5)
        # plt.show()  # Mostra o gráfico


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
        imprimeCaminho(item, 20, 'green')

    # Percorre a lista de caminhos de menor probabilidade
    for item in sub_mapa_menor_proba:
        imprimeCaminho(item, 20, 'red')

    print('\tCaminhos mais prováveis: em verde')
    print('\tCaminhos menos prováveis: em vermelho.')

    configGraficos()

    print('REFERÊNCIA 1 ----------------------------------------------------------------------')

    # Função que recebe o mapa do tabuleiro (fornecido pela função mapaTabuleiro()), a lista
    # de distintas probabilidades (fornecida pelo método distintasProbas()), o menor valor de
    # probabilidade desejado, o maior valor desejado e retorna uma lista com todos os caminhos na
    # faixa de probabilidades entre o menor e o maior valor inseridos.
    def mapaFaixaProbas(mapa_tabuleiro, distintas_probas, indice_min_proba, indice_max_proba):
        distintas_probas.sort()
        inf = distintas_probas[indice_min_proba]
        sup = distintas_probas[indice_max_proba]
        caminhos = []  # Lista que recebe os caminhos na faixa de probabilidades escolhida.
        for item in mapa_tabuleiro:  # "item" é guardado na lista quando sua probabilidade ...
            if inf <= item[1] < sup:  # ... está entre a menor e a maior.
                caminhos.append(item)
        return caminhos


    submapa_inferior = mapaFaixaProbas(mapa_tabuleiro, distintas_probas, 0, 4000)
    submapa_superior = mapaFaixaProbas(mapa_tabuleiro, distintas_probas, 19076, 23076)

    print('REFERÊNCIA 2 ----------------------------------------------------------------------')

    # Percorre a lista de caminhos de maior probabilidade e imprime cada um.
    for caminho in submapa_superior:
        imprimeCaminho(caminho, 1, 'green')

    # Percorre a lista de caminhos de menor probabilidade e imprime cada um.
    for caminho in submapa_inferior:
        imprimeCaminho(caminho, 1, 'red')

    print('\tCaminhos mais prováveis: em verde')
    print('\tCaminhos menos prováveis: em vermelho.')

    configGraficos()

    print('REFERÊNCIA 3 ----------------------------------------------------------------------')

    # Percorre a lista de caminhos de menor probabilidade, imprime cada um e conta.
    total_vermelho = 0
    for caminho in submapa_inferior:
        imprimeCaminho(caminho, 1, 'red')
        total_vermelho += 1

    # Percorre a lista de caminhos de maior probabilidade, imprime cada um e conta.
    total_verde = 0
    for caminho in submapa_superior:
        imprimeCaminho(caminho, 1, 'green')
        total_verde += 1

    print(f'\tCaminhos mais prováveis: em verde ({total_verde} caminhos)')
    print(f'\tCaminhos menos prováveis: em vermelho ({total_vermelho} caminhos)')

    configGraficos()

    print('REFERÊNCIA 4 ----------------------------------------------------------------------')

    # Função que percorre uma lista de caminhos em uma faixa de probabilidades
    # e retorna uma lista contendo uma quantidade aleatória de caminhos.
    def subMapaAleatorio(submapa, quantidade):
        lista = []
        if len(submapa) >= quantidade:
            for caminho in rd.sample(submapa, quantidade):
                lista.append(caminho)
        return lista


    # Função que recebe dois submapas e retorna o número de elementos do menor.
    def total(submapa_inferior, submapa_superior):
        linf = len(submapa_inferior)
        lsup = len(submapa_superior)
        if linf < lsup:
            return linf
        return lsup


    # Percorre mapa das maiores probabilidades contando cada casa, faz o mesmo com as mais baixas
    # e retorna um novo mapeamento com a razão entre o total de mais altas pelo total de mais baixas.
    def mapaRazoes(submapa_inferior, submapa_superior):
        tab_razoes = [[[1, 1] for _ in range(9)] for _ in range(11)]
        razoes = [[1 for _ in range(9)] for _ in range(11)] # Esta linha substitui a representação anterior.
        for caminho_prob in submapa_inferior:  # Para cada par (caminho, probabilidade_do_caminho) no mapa inferior.
            caminho = caminho_prob[0]
            for casa in caminho:
                lin = casa[0]
                col = casa[1]
                tab_razoes[lin][col][1] += 1
        for caminho_prob in submapa_superior:  # Para cada par (caminho, probabilidade_do_caminho) no mapa superior.
            caminho = caminho_prob[0]
            for casa in caminho:
                lin = casa[0]
                col = casa[1]
                tab_razoes[lin][col][0] += 1
        for l in range(11):
            for c in range(9):
                razoes[l][c] = tab_razoes[l][c][0] / tab_razoes[l][c][1]
        return razoes


    # Método que recebe uma lista contendo mapas de razões e retorna um tabuleiro contendo
    # as médias das razões dos tabuleiros inseridos para cada casa.
    def mediasRazoes(lista_mapas_razoes):
        tam = len(lista_mapas_razoes)
        medias = [[0 for _ in range(9)] for _ in range(11)]  # Tabuleiro inicializado com 0's.
        for mapa_razoes in lista_mapas_razoes:
            for i in range(11):
                for j in range(9):
                    medias[i][j] += mapa_razoes[i][j]
        for i in range(11):
            for j in range(9):
                medias[i][j] = medias[i][j] / tam
        return medias


    # Método que recebe uma lista contendo mapas de razões, o mapa das médias
    # da lista e retorna um tabuleiro contendo os desvios das médias das razões para cada casa.
    def desviosRazoes(lista_mapas_razoes, medias):
        tam = len(lista_mapas_razoes)
        desvios = [[0 for _ in range(9)] for _ in range(11)]  # Tabuleiro inicializado com 0's.
        for mapa_razoes in lista_mapas_razoes:
            for i in range(11):
                for j in range(9):
                    desvios[i][j] += abs(mapa_razoes[i][j] - medias[i][j])
        for i in range(11):
            for j in range(9):
                desvios[i][j] = desvios[i][j] / tam
        return desvios


    # Função que recebe uma lista contendo as médias das razões, o mapa dos desvios das médias
    # e retorna um tabuleiro contendo as médias com os desvios adicionados ou subtraídos para cada casa,
    # dependendo do parâmetro sup ser True ou False, respectivamente.
    def mediasComDesvio(medias, desvios, sup):
        medias_desvio = [[0 for _ in range(9)] for _ in range(11)]  # Tabuleiro inicializado com 0's.
        if sup:  # sup vale True.
            for i in range(11):
                for j in range(9):
                    medias_desvio[i][j] = medias[i][j] + desvios[i][j]
        else:  # sup vale False.
            for i in range(11):
                for j in range(9):
                    medias_desvio[i][j] = medias[i][j] - desvios[i][j]
        return medias_desvio


    # Verifica qual submapa possui menor número de elementos para imprimir a mesma quantidade.
    TOTAL = total(submapa_inferior, submapa_superior)

    # Gera diversos mapas de razões do tabuleiro e guarda na lista de mapas de razões.
    lista_mapas_razoes = []
    for _ in range(4000):
        submapa_aleatorio_superior = subMapaAleatorio(submapa_superior, TOTAL)
        submapa_aleatorio_inferior = subMapaAleatorio(submapa_inferior, TOTAL)
        razoes = mapaRazoes(submapa_aleatorio_inferior, submapa_aleatorio_superior)
        lista_mapas_razoes.append(razoes)

    print('REFERÊNCIA 5 ----------------------------------------------------------------------')

    # Mapa com as médias (por casa) das razões na lista de mapas de razões.
    medias = mediasRazoes(lista_mapas_razoes)

    # Mapa com os desvios (por casa) das médias das razões na lista de mapas de razões.
    desvios = desviosRazoes(lista_mapas_razoes, medias)

    # Médias menos os desvios (indicado pelo False):
    medias_inf = mediasComDesvio(medias, desvios, False)

    # Médias mais os desvios (indicado pelo True):
    medias_sup = mediasComDesvio(medias, desvios, True)

    print(f'Médias inferiores (primeira linha):\n{medias_inf[0]}\n')

    print(f'Médias (primeira linha):\n{medias[0]}\n')

    print(f'Médias superiores (primeira linha):\n{medias_sup[0]}')

    fig = plt.figure()
    ax1 = fig.add_subplot(1, 3, 1)  # Infográfico das médias inferiores.
    ax2 = fig.add_subplot(1, 3, 2)  # Infográfico das médias.
    ax3 = fig.add_subplot(1, 3, 3)  # Infográfico das médias superiores.

    VMAX = 10  # Valor máximo para a normalização.

    # Coloração do infográfico das médias inferiores:
    im = ax1.pcolor(medias_inf, cmap="viridis_r", vmin=0, vmax=VMAX)
    ax1.set_title('Médias Inferiores\n', fontsize=18)

    # Coloração do infográfico das médias:
    ax2.pcolor(medias, cmap="viridis_r", vmin=0, vmax=VMAX)
    ax2.set_title('Médias\n', fontsize=18)

    # Coloração do infográfico das médias superiores:
    ax3.pcolor(medias_sup, cmap="viridis_r", vmin=0, vmax=VMAX)
    ax3.set_title('Médias Superiores\n', fontsize=18)

    plt.colorbar(im)  # Escala de cores.

    plt.subplots_adjust(right=3, wspace=0.3)

    # plt.show()

    print('REFERÊNCIA 6 ----------------------------------------------------------------------')

    media_esquerda = []
    media_centro = []
    media_direita = []
    for linha in tab_proba:
        for coluna in range(0, 3):
            media_esquerda.append(linha[coluna][3])
        for coluna in range(3, 6):
            media_centro.append(linha[coluna][3])
        for coluna in range(6, 9):
            media_direita.append(linha[coluna][3])

    media_esquerda = sum(media_esquerda) / 33  # 33 é o número de casas em cada região.
    media_centro = sum(media_centro) / 33
    media_direita = sum(media_direita) / 33

    print(f'Média das probabilidades na região esquerda: {round(media_esquerda, 4)}')
    print(f'Média das probabilidades na região central: {round(media_centro, 4)}')
    print(f'Média das probabilidades na região direita: {round(media_direita, 4)}')

    probas = [[0 for _ in range(9)] for _ in range(11)]
    for i in range(11):
        for j in range(9):
            probas[i][j] = tab_proba[i][j][3]
    plt.pcolor(probas, cmap="viridis_r", vmin=0, vmax=0.1)
    plt.title('Probabilidades no Tabuleiro\n', fontsize=14)
    # plt.show()

    print('REFERÊNCIA 7 ----------------------------------------------------------------------')

    # Modelo do tabuleiro:
    tab = [
        [7, 5, 6, 9, 4, 2, 8, 1, 3],  # linha 1  = tab[0]  - Início do jogo
        [2, 8, 1, 8, 10, 7, 9, 4, 5],  # linha 2  = tab[1]
        [7, 3, 2, 1, 5, 4, 5, 7, 3],  # linha 3  = tab[2]
        [5, 8, 7, 2, 8, 7, 6, 9, 8],  # linha 4  = tab[3]
        [7, 3, 2, 1, 5, 4, 5, 7, 3],  # linha 5  = tab[4]
        [2, 4, 8, 5, 9, 7, 6, 8, 5],  # linha 6  = tab[5]
        [8, 7, 3, 6, 4, 1, 2, 5, 1],  # linha 7  = tab[6]
        [6, 2, 5, 7, 8, 7, 6, 4, 3],  # linha 8  = tab[7]
        [8, 7, 6, 3, 5, 4, 9, 2, 7],  # linha 9  = tab[8]
        [5, 4, 3, 8, 9, 1, 2, 5, 4],  # linha 10 = tab[9]
        [2, 9, 7, 4, 6, 8, 7, 5, 9],  # linha 11 = tab[10] - Fim do jogo
    ]

    tab_esquerda = [
        [7, 5, 6],  # linha 1  = tab[0]  - Início do jogo
        [2, 8, 1],  # linha 2  = tab[1]
        [7, 3, 2],  # linha 3  = tab[2]
        [5, 8, 7],  # linha 4  = tab[3]
        [7, 3, 2],  # linha 5  = tab[4]
        [2, 4, 8],  # linha 6  = tab[5]
        [8, 7, 3],  # linha 7  = tab[6]
        [6, 2, 5],  # linha 8  = tab[7]
        [8, 7, 6],  # linha 9  = tab[8]
        [5, 4, 3],  # linha 10 = tab[9]
        [2, 9, 7],  # linha 11 = tab[10] - Fim do jogo
    ]

    tab_centro = [
        [9, 4, 2],  # linha 1  = tab[0]  - Início do jogo
        [8, 10, 7],  # linha 2  = tab[1]
        [1, 5, 4],  # linha 3  = tab[2]
        [2, 8, 7],  # linha 4  = tab[3]
        [1, 5, 4],  # linha 5  = tab[4]
        [5, 9, 7],  # linha 6  = tab[5]
        [6, 4, 1],  # linha 7  = tab[6]
        [7, 8, 7],  # linha 8  = tab[7]
        [3, 5, 4],  # linha 9  = tab[8]
        [8, 9, 1],  # linha 10 = tab[9]
        [4, 6, 8],  # linha 11 = tab[10] - Fim do jogo
    ]

    tab_direita = [
        [8, 1, 3],  # linha 1  = tab[0]  - Início do jogo
        [9, 4, 5],  # linha 2  = tab[1]
        [5, 7, 3],  # linha 3  = tab[2]
        [6, 9, 8],  # linha 4  = tab[3]
        [5, 7, 3],  # linha 5  = tab[4]
        [6, 8, 5],  # linha 6  = tab[5]
        [2, 5, 1],  # linha 7  = tab[6]
        [6, 4, 3],  # linha 8  = tab[7]
        [9, 2, 7],  # linha 9  = tab[8]
        [2, 5, 4],  # linha 10 = tab[9]
        [7, 5, 9],  # linha 11 = tab[10] - Fim do jogo
    ]


    # Função que recebe um tabuleiro reduzido (com 3 colunas) e testa uma jogada, retornando a quantidade de jogadas
    # onde não foi possível avançar por falta de opção. O parâmetro imprimir, imprime a sequência de jogadas
    # quando vale True e, caso contrário, apenas retorna a quantidade de jogadas.
    def jogar(tabuleiro, configuracoes_dados, imprimir):
        passou = 0  # Contador de jogadas sem avançar.
        coluna = rd.randint(0, 2)  # Escolha aleatória de coluna do tabuleiro para começar.
        pos_inicial = (0, coluna)  # Posição inicial no tabuleiro, iniciando na 1ª linha e em coluna aleatória.

        i = 0  # Índice para a primeira linha do tabuleiro, ou seja, posição zero.

        while i < len(tabuleiro) - 1:
            # O parâmetro "configuracoes" fornece todas as possíveis configurações para três dados distintos.
            jogada = rd.sample(configuracoes_dados, 1)  # Lança os três dados.

            expressoes = resultadosExpressoes(
                jogada)  # Lista de todas as possíveis expressões numéricas para a "jogada" acima.

            proxima_jogada = listaProximaJogada(pos_inicial[1], 2)

            possibilidades = []  # Lista que guarda as possíveis casas para avançar, i. e., as casas da linha seguinte
            # que possuem resultados na lista "expressoes".

            for posicao in proxima_jogada:
                for expressao in expressoes:
                    if expressao == tabuleiro[i + 1][posicao]:
                        possibilidades.append(expressao)

            if imprimir:
                print(f'Posição inicial: {pos_inicial}')
                print(f'Jogada: {jogada}')
                print(f'Expressões: {expressoes}')
                print(f'Lista da próxima jogada: {proxima_jogada}')
                print(f'Próxima linha: {tabuleiro[i + 1]}')

            if possibilidades:  # Se há possibilidades de avançar, escolhe aleatoriamente a próxima casa.
                escolha = rd.choice(possibilidades)  # Escolhe um número na próxima linha para avançar.
                coluna = tabuleiro[i + 1].index(escolha)  # Verifica, na próxima linha, qual é a coluna referente ao
                # número escolhido para avançar.
                i += 1  # Avança para a próxima linha.
            else:
                passou += 1

            if imprimir:
                print(f'Possibilidades: {possibilidades}')
                print(f'Jogadas sem avançar: {passou}\n')

            pos_inicial = (i, coluna)  # Avança para a próxima linha, na coluna escolhida acima.

        return passou


    # Teste para visualizar (indicado pelo True) uma sequência de jogadas por uma região
    # do tabuleiro de teste, usado no início do texto.
    # Modelo do tabuleiro de teste:
    tab_teste = [
        [7, 5, 6],  # linha 1 = tab[0] - Início do jogo
        [2, 8, 1],  # linha 2 = tab[1]
        [7, 3, 2],  # linha 3 = tab[2]
        [5, 8, 7],  # linha 4 = tab[3] - Fim do jogo
    ]
    print(f'\nTotal de jogadas sem avançar: {jogar(tab_teste, configuracoes_dados, True)}')

    import numpy as np
    import pandas as pd


    def simulacao(numero_testes):
        esquerda = []
        centro = []
        direita = []
        for _ in range(numero_testes):
            esquerda.append(jogar(tab_esquerda, False))
            centro.append(jogar(tab_centro, False))
            direita.append(jogar(tab_direita, False))
        esquerda = sum(esquerda) / numero_testes
        centro = sum(centro) / numero_testes
        direita = sum(direita) / numero_testes
        return (esquerda, centro, direita)


    print('REFERÊNCIA 8 ----------------------------------------------------------------------')

    dados = np.array([simulacao(10),
                      simulacao(100),
                      simulacao(1000),
                      simulacao(10000),
                      simulacao(100000),
                      simulacao(1000000),
                      simulacao(10000000),
                      simulacao(100000000),])

    df = pd.DataFrame(dados,
                      index=['Dez', 'Cem', 'Mil', 'Dez Mil', 'Cem Mil', 'Um Milhão', 'Dez Milhões', 'Cem Milhões'],
                      columns=['Esquerda', 'Centro', 'Direita'])

    print(f'\n{df}')

    print(f'{df.mean()}')

    # Percentual a mais do centro com relação a esquerda:
    df['% Centro'] = 100 * (df['Centro'] - df['Esquerda']) / df['Esquerda']

    # Percentual a mais da direita com relação a esquerda:
    df['% Direita'] = 100 * (df['Direita'] - df['Esquerda']) / df['Esquerda']

    # Remove as colunas Esquerda, Centro e Direita da nova visualização:
    percentual = df.drop(['Esquerda', 'Centro', 'Direita'], axis=1)

    print(f'\n{percentual}')

    print(f'{percentual.mean()}')

    def totalCaminhos():
        # Modelo do tabuleiro:
        tab = [
            [7, 5, 6, 9, 4, 2, 8, 1, 3],  # linha 1  = tab[0]  - Início do jogo
            [2, 8, 1, 8, 10, 7, 9, 4, 5],  # linha 2  = tab[1]
            [7, 3, 2, 1, 5, 4, 5, 7, 3],  # linha 3  = tab[2]
            [5, 8, 7, 2, 8, 7, 6, 9, 8],  # linha 4  = tab[3]
            [7, 3, 2, 1, 5, 4, 5, 7, 3],  # linha 5  = tab[4]
            [2, 4, 8, 5, 9, 7, 6, 8, 5],  # linha 6  = tab[5]
            [8, 7, 3, 6, 4, 1, 2, 5, 1],  # linha 7  = tab[6]
            [6, 2, 5, 7, 8, 7, 6, 4, 3],  # linha 8  = tab[7]
            [8, 7, 6, 3, 5, 4, 9, 2, 7],  # linha 9  = tab[8]
            [5, 4, 3, 8, 9, 1, 2, 5, 4],  # linha 10 = tab[9]
            [2, 9, 7, 4, 6, 8, 7, 5, 9],  # linha 11 = tab[10] - Fim do jogo
        ]
        colunaMAX = 8  # Maior índice das colunas do tabuleiro.
        caminhos = []  # Lista para receber os caminhos.
        # Determina todos os possíveis caminhos no tabuleiro 11 X 9:
        for p1 in [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # p1 é a posição na linha 1,
            for p2 in listaProximaJogada(p1, colunaMAX):  # p2 é a posição na linha 2, etc.
                for p3 in listaProximaJogada(p2, colunaMAX):
                    for p4 in listaProximaJogada(p3, colunaMAX):
                        for p5 in listaProximaJogada(p4, colunaMAX):
                            for p6 in listaProximaJogada(p5, colunaMAX):
                                for p7 in listaProximaJogada(p6, colunaMAX):
                                    for p8 in listaProximaJogada(p7, colunaMAX):
                                        for p9 in listaProximaJogada(p8, colunaMAX):
                                            for p10 in listaProximaJogada(p9, colunaMAX):
                                                for p11 in listaProximaJogada(p10, colunaMAX):
                                                    caminhos.append([tab[0][p1], tab[1][p2],
                                                                     tab[2][p3], tab[3][p4],
                                                                     tab[4][p5], tab[5][p6],
                                                                     tab[6][p7], tab[7][p8],
                                                                     tab[8][p9], tab[9][p10],
                                                                     tab[10][p11]]
                                                                    )
        return caminhos


    print(f'Total de caminhos distintos no tabuleiro 11 X 9: {len(totalCaminhos())}')

    resultados_distintos = []  # Lista para guardar todos os distintos resultados das
    # expressões numéricas que compõe o espaço amostral.

    for resultado in resultados_expressoes:  # Percorre a lista dos 308 resultados do espaço amostral.
        if resultado not in resultados_distintos:
            resultados_distintos.append(resultado)  # Adiciona à lista apenas os resultados distintos.

    soma = 0  # Variável para acumular a soma das probabilidades.
    for evento in resultados_distintos:  # Percorre a lista dos 30 resultados distintos de eventos simples.
        soma += probabilidade(evento, resultados_expressoes)

    print(f'Soma das probabilidades: {soma}\n')
