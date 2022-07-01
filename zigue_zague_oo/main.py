from matplotlib import pyplot as plt
import ziguezague

if __name__ == "__main__":
    # CONFIGURAÇÕES INICIAIS
    zz = ziguezague.ZigueZague()  # Instancia a classe ZigueZague().
    mapa_tabuleiro = zz.mapaTabuleiro()  # Faz o mapeamento do tabuleiro.
    distintas_probas = zz.distintasProbas(mapa_tabuleiro)  # Avalia os distintos valores de probabilidades no tabuleiro.
    submapa_inferior = zz.mapaFaixaProbas(mapa_tabuleiro, distintas_probas, 0, 1000)
    submapa_superior = zz.mapaFaixaProbas(mapa_tabuleiro, distintas_probas, 22076, 23076)
    # FIM DAS CONFIGURAÇÕES INICIAIS

    # Verifica qual submapa possui menor número de elementos para imprimir a mesma quantidade.
    TOTAL = zz.total(submapa_inferior, submapa_superior)

    # Gera diversos mapas de razões do tabuleiro e guarda na lista de mapas de razões.
    lista_mapasRazoes = []
    for _ in range(10):
        submapa_aleatorio_superior = zz.subMapaAleatorio(submapa_superior, TOTAL)
        submapa_aleatorio_inferior = zz.subMapaAleatorio(submapa_inferior, TOTAL)
        razoes = zz.mapaRazoes(submapa_aleatorio_inferior, submapa_aleatorio_superior)
        lista_mapasRazoes.append(razoes)

    # Mapa com as médias (por casa) das razões na lista de mapas de razões.
    medias = zz.mediasRazoes(lista_mapasRazoes)

    # Mapa com os desvios (por casa) das médias das razões na lista de mapas de razões.
    desvios = zz.desviosRazoes(lista_mapasRazoes, medias)

    medias_inf = zz.mediasComDesvio(medias, desvios, False)  # Médias menos (indicado pelo False) os desvios.
    medias_sup = zz.mediasComDesvio(medias, desvios, True)  # Médias mais (indicado pelo True) os desvios.

    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax2.pcolor(medias_inf, cmap="viridis_r", vmin=0, vmax=10)
    ax1.pcolor(medias, cmap="viridis_r", vmin=0, vmax=10)
    ax3.pcolor(medias_sup, cmap="viridis_r", vmin=0, vmax=10)
    plt.show()

    # zz.imprimeRazoes(medias_inf, ax1)
    # zz.imprimeRazoes(medias, ax2)
    # zz.imprimeRazoes(medias_sup, ax3)
    #
    # tab_proba = zz.tabProba()
    # probas = [[0 for _ in range(9)] for _ in range(11)]
    # for i in range(11):
    #     for j in range(9):
    #         probas[i][j] = tab_proba[i][j][3]
    # zz.imprimeRazoes(probas, ax4)
    #
    # zz.configGraficos()

    # # Gera submapas aleatórios.
    # submapa_aleatorio_inferior = zz.subMapaAleatorio(submapa_inferior, TOTAL)
    # submapa_aleatorio_superior = zz.subMapaAleatorio(submapa_superior, TOTAL)
    #
    # # Cria a lista de razões entre o total de caminhos de mais alta probabilidade que passam por uma casa e
    # # o total de caminhos de mais baixa probabilidade que passam pela mesma casa, para cada casa do tabuleiro.
    # razoes = zz.mapaRazoes(submapa_aleatorio_inferior, submapa_aleatorio_superior)
    #
    # # Imprime um retângulo para cada casa do tabuleiro, de modo que a cor do retângulo seja "proporcional" ao
    # # respectivo valor na lista de razões; quanto mais alto o valor na casa, mais escuro o retângulo.
    # zz.imprimeRazoes(razoes)
    #
    # # Percorre a sublista de caminhos aleatórios na lista de menores probabilidades.
    # for caminho in submapa_aleatorio_inferior:
    #     zz.imprimeCaminho(caminho, 1, 'red')
    #
    # # Percorre a sublista de caminhos aleatórios na lista de maiores probabilidades.
    # for caminho in submapa_aleatorio_superior:
    #     zz.imprimeCaminho(caminho, 1, 'green')
    #
    # # Configura o gráfico.
    # zz.configGraficos()