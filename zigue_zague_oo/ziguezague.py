from itertools import permutations, product
import random as rd
from matplotlib import pyplot as plt, cm

class ZigueZague:

    def listaProximaJogada(self, posicaoAtual, colunaMAX):
        """ Método para determinar o intervalo de casas possíveis de avançar na próxima linha.
            Argumento: Posição atual.
            Saída: Lista (de 2 ou 3 elementos) contendo a sequência de casas possíveis. """
        if posicaoAtual == 0:
            return [0, 1]
        elif posicaoAtual == colunaMAX:
            return [colunaMAX - 1, colunaMAX]
        elif 0 < posicaoAtual < colunaMAX:
            return [posicaoAtual - 1, posicaoAtual, posicaoAtual + 1]
        else:
            return []

    def totalCaminhosTeste(self):
        """ Percorre o tabuleiro de teste, capturando todos os possíveis caminhos e retorna uma
            lista com os mesmos. """
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
            for p2 in self.listaProximaJogada(p1, colunaMAX):
                for p3 in self.listaProximaJogada(p2, colunaMAX):
                    for p4 in self.listaProximaJogada(p3, colunaMAX):
                        caminhos.append([tab[0][p1], tab[1][p2], tab[2][p3], tab[3][p4]])
        return caminhos

    def produtoFiltrado(self):
        """ Método que retorna a lista de todos os possíveis resultados no lançamento de 3 dados. """
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

    def resultadosExpressoes(self, configuracoes_dados):
        """ Método que retorna todos os possíveis resultados de todas as expressões
            numéricas obtidas com as coordenadas de cada terna obtida no experimento aleatório. """
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

    def cardinalidade(self, evento, configuracoes_dados):
        """ Método que recebe a lista com todas as possíveis configurações dos dados e
            retorna a cardinalidade de qualquer um dos eventos. """
        cardinalidade = 0
        for r in self.resultadosExpressoes(configuracoes_dados):
            if r == evento:
                cardinalidade += 1
        return cardinalidade

    def probabilidade(self, evento, configuracoes_dados):
        """ Método para calcular a probabilidade de um evento. """
        resultados = self.resultadosExpressoes(configuracoes_dados)
        cardinalidade = self.cardinalidade(evento, configuracoes_dados)
        return cardinalidade / len(resultados)

    def tabProba(self, configuracoes_dados):
        """ Retorna uma lista "tabuleiro de probabilidades", contendo (linha, coluna, valor, probabilidade). """
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
        tab_proba = [[] for _ in range(11)]
        for lin in range(len(tab)):  # Percorre as linhas no tabuleiro.
            for col in range(len(tab[0])):  # Percorre as colunas em cada linha.
                tab_proba[lin].append([lin, col, tab[lin][col], self.probabilidade(tab[lin][col], configuracoes_dados)])
                # Na linha acima, é calculada e adicionada a quadra (lin, col, valor, probabilidade)
                # ao tabuleiro de probabilidades, onde lin indica a linha e col a coluna.
        return tab_proba

    def probaCaminho(self, caminho):
        """ Método que recebe um caminho e retorna sua probabilidade. """
        produto = 1  # variável que será retornada com a probabilidade do caminho.
        for item in caminho:
            produto *= item[3]
        return produto

    def mapaTabuleiro(self, tab_proba):
        """ Método que calcula as probabilidades de cada caminho e retorna uma lista com
            os pares (caminho, probabilidade do caminho). """
        colunaMAX = 8  # Guarda o maior índice de coluna do tabuleiro.
        mapa = []  # Lista vazia para receber os pares (caminho, probabilidade do caminho).
        # Determina todos os possíveis caminhos no tabuleiro 11 X 9:
        for p1 in [0, 1, 2, 3, 4, 5, 6, 7, 8]:  # p1 é a posição na linha 1,
            for p2 in self.listaProximaJogada(p1, colunaMAX):  # p2 é a posição na linha 2, etc.
                for p3 in self.listaProximaJogada(p2, colunaMAX):
                    for p4 in self.listaProximaJogada(p3, colunaMAX):
                        for p5 in self.listaProximaJogada(p4, colunaMAX):
                            for p6 in self.listaProximaJogada(p5, colunaMAX):
                                for p7 in self.listaProximaJogada(p6, colunaMAX):
                                    for p8 in self.listaProximaJogada(p7, colunaMAX):
                                        for p9 in self.listaProximaJogada(p8, colunaMAX):
                                            for p10 in self.listaProximaJogada(p9, colunaMAX):
                                                for p11 in self.listaProximaJogada(p10, colunaMAX):
                                                    caminho = [
                                                        tab_proba[0][p1], tab_proba[1][p2],
                                                        tab_proba[2][p3], tab_proba[3][p4],
                                                        tab_proba[4][p5], tab_proba[5][p6],
                                                        tab_proba[6][p7], tab_proba[7][p8],
                                                        tab_proba[8][p9], tab_proba[9][p10],
                                                        tab_proba[10][p11]
                                                    ]
                                                    proba = self.probaCaminho(caminho)
                                                    mapa.append((caminho, proba))
        return mapa

    def distintasProbas(self, mapa_tabuleiro):
        """ Método que retorna uma lista com todos os diferentes valores de probabilidades
            encontrados no mapeamento do tabuleiro. """
        distintas_probas = []  # Guarda os distintos valores de probabilidades dos caminhos.
        for caminho in mapa_tabuleiro:
            if caminho[1] not in distintas_probas:
                distintas_probas.append(caminho[1])
        return distintas_probas

    def valoresExtremos(self, lista_distintas_probas):
        """ Retorna o maior e o menor valor para as probabilidades dos caminhos. """
        tam = len(lista_distintas_probas)
        lista_distintas_probas.sort()  # Ordena distintas_probas do menor para o maior elemento.
        menor_proba = lista_distintas_probas[0]
        maior_proba = lista_distintas_probas[tam - 1]
        return [menor_proba, maior_proba]

    def valorAleatorio(self):
        """ Método que retorna um número aleatório entre 0.15 e 0.85. """
        acrescimo = rd.random()
        if acrescimo > 0.85:
            acrescimo = 0.85
        elif acrescimo < 0.15:
            acrescimo = 0.15
        return acrescimo
        # numero = rd.randint(150000, 850000)
        # return 0.000001 * numero

    def imprimeCaminho(self, sub_mapa_tabuleiro, tamanho, cor):
        """ Imprime todos os caminhos em qualquer sub-mapa do mapeamento do tabuleiro. Devendo
            ser inseridos os parâmetros submapa, tamanho e cor. """
        coord_lin = []
        coord_col = []
        caminho = sub_mapa_tabuleiro[0]  # Caminho no mapeamento
        for posicao in caminho:  # Para cada posição ocupada no tabuleiro
            coord_lin.append(posicao[0] + self.valorAleatorio())  # Grava linha + acréscimo em coord_lin
            coord_col.append(posicao[1] + self.valorAleatorio())  # Grava coluna + acréscimo em coord_col
            # coord_lin.append(posicao[0] + 0.000001 * rd.randint(150000, 850000))  # Grava linha + acréscimo em coord_lin
            # coord_col.append(posicao[1] + 0.000001 * rd.randint(150000, 850000))  # Grava coluna + acréscimo em coord_col
        plt.scatter(coord_col, coord_lin, color=cor, marker='s', s=tamanho)  # Imprime os pontos no gráfico

    def configGraficos(self):
        """ Gera a configuração para a impressão dos infográficos, de modo que o tabuleiro do
            Zigue-Zague seja representado. """
        plt.xlabel("Colunas", fontsize=14)
        plt.ylabel("Linhas", fontsize=14)
        plt.xticks(range(0, 10))
        plt.yticks(range(0, 12))
        plt.grid(color='black', linestyle='solid', linewidth=0.5)
        plt.show()  # Mostra o gráfico

    def mapaFaixaProbas(self, mapeamento, lista_distintas_probas, indice_min_proba, indice_max_proba):
        """ Método que recebe o mapa do tabuleiro (fornecido pelo método mapaTabuleiro()), a lista
            de distintas probabilidades (fornecida pelo método distintasProbas()), o menor valor de
            probabilidade desejado, o maior valor desejado e retorna uma lista com todos os caminhos na
            faixa de probabilidades entre o menor e o maior valor inseridos. """
        lista_distintas_probas.sort()
        inf = lista_distintas_probas[indice_min_proba]
        sup = lista_distintas_probas[indice_max_proba]
        caminhos = []  # Lista que recebe os caminhos na faixa de probabilidades escolhida.
        for item in mapeamento:  # "item" é guardado na lista quando sua probabilidade ...
            if inf <= item[1] < sup:  # ... está entre a menor e a maior.
                caminhos.append(item)
        return caminhos

    def subMapaAleatorio(self, submapa, quantidade):
        """ Método que percorre uma lista de caminhos em uma faixa de probabilidades e imprime uma
            quantidade aleatoriamente. """
        lista = []
        if len(submapa) >= quantidade:
            for caminho in rd.sample(submapa, quantidade):
                lista.append(caminho)
        return lista

    def total(self, submapa_inferior, submapa_superior):
        """ Método que recebe dois submapas e retorna o número de elementos do menor. """
        linf = len(submapa_inferior)
        lsup = len(submapa_superior)
        if linf < lsup:
            return linf
        return lsup

    def mapaRazoes(self, submapa_inferior, submapa_superior):
        """ Percorre mapa das maiores probabilidades contando cada casa, faz o mesmo com as mais baixas
            e retorna um novo mapeamento com a razão entre o total de mais altas pelo total de mais baixas. """
        tab_razoes = [[[1, 1] for _ in range(9)] for _ in range(11)]
        razoes = [[1 for _ in range(9)] for _ in range(11)]
        for caminho_prob in submapa_inferior:  # Para cada par (caminho, probabilidade_do_caminho) no mapa inferior...
            caminho = caminho_prob[0]
            for casa in caminho:
                lin = casa[0]
                col = casa[1]
                tab_razoes[lin][col][1] += 1
        for caminho_prob in submapa_superior:  # Para cada par (caminho, probabilidade_do_caminho) no mapa superior...
            caminho = caminho_prob[0]
            for casa in caminho:
                lin = casa[0]
                col = casa[1]
                tab_razoes[lin][col][0] += 1
        for l in range(11):
            for c in range(9):
                razoes[l][c] = tab_razoes[l][c][0] / tab_razoes[l][c][1]
        return razoes

    def imprimeRazoes(self, mapa_razoes, posicao):
        """ Método que recebe um mapa de razões, uma posição de impressão e retorna a impressão do infográfico
        que representa as probabilidades no tabuleiro. """
        leque_cores = cm.get_cmap('viridis_r', 99)
        mapa_array = []
        for lin in range(11):
            for col in range(9):
                mapa_array.append((lin, col, mapa_razoes[lin][col]))
        coord_lin = []
        coord_col = []
        razoes = []
        for item in mapa_array:
            coord_lin.append(item[0] + 0.5)
            coord_col.append(item[1] + 0.5)
            razoes.append(item[2])
        posicao.scatter(coord_col, coord_lin, c=razoes, vmin=0, vmax=5, cmap=leque_cores, marker='s', s=1500)

    def mediasRazoes(self, lista_mapas_razoes):
        """ Método que recebe uma lista contendo mapas de razões e retorna um tabuleiro contendo
            as médias das razões dos tabuleiros inseridos para cada casa. """
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

    def desviosRazoes(self, lista_mapas_razoes, medias):
        """ Método que recebe uma lista contendo mapas de razões, o mapa das médias
            da lista e retorna um tabuleiro contendo os desvios das médias das razões para cada casa. """
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

    def mediasComDesvio(self, medias, desvios, sup):
        """ Método que recebe uma lista contendo as médias das razões, o mapa dos desvios das médias
            e retorna um tabuleiro contendo as médias com os desvios adicionados ou subtraídos para cada casa,
            dependendo do parâmetro sup ser True ou False, respectivamente. """
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
