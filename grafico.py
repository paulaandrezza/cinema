class Grafico():
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  def ingressos_filme(self):
    self.cursor.execute(" SELECT FILME.nome, COUNT(INGRESSO.idIngresso) AS quantidade_vendida FROM FILME JOIN SESSAO ON FILME.idFilme = SESSAO.idFilme JOIN INGRESSO ON SESSAO.idSessao = INGRESSO.idSessao GROUP BY FILME.idFilme, FILME.nome")
    resultados = self.cursor.fetchall()
    nomes_filmes = []
    quantidades_vendidas = []

    for filme, quantidade in resultados:
        nomes_filmes.append(filme)
        quantidades_vendidas.append(quantidade)

    return nomes_filmes, quantidades_vendidas

"""
    filmes = f"SELECT nome"
    ingressos = f"SELECT COUNT(INGRESSO.idIngresso) AS quantidade_vendida FROM FILME JOIN SESSAO ON FILME.idFilme = SESSAO.idFilme JOIN INGRESSO ON SESSAO.idSessao = INGRESSO.idSessao GROUP BY FILME.idFilme"

    cat_com_desp = []
    id_categorias = []
    valores = []
    for i in valor_por_cat_despesa:
      cat_com_desp.append(valor_por_cat_despesa[i][1])
      i += 1 
    i = 0
    for i in cat_por_nome:
      id_categorias.append(cat_por_nome[i][0])
      i += 1
    i = 0
    for i in valor_por_cat_despesa:
      valores.append(valor_por_cat_despesa[i][0])
      i += 1 
    desp_nome = []
    for i in range(len(cat_com_desp)):
      if cat_com_desp[i] in id_categorias:
        j = cat_com_desp[i]
        pos = id_categorias.index(j)
        desp_nome.append(cat_por_nome[pos][1])
    ax.bar(nomes, idades, label=bar_labels, color=bar_colors)
    ax.set_ylabel('Nomes')
    ax.set_title('Nomes e idades')
    ax.legend(title='Nomes idades coloridas')

    plt.show()


nomes = ['Erick', 'Pedro', 'Thaisa', 'Thabata', 'Michelly', 'Paula']
idades = [18, 19, 19, 18, 20, 23]
bar_labels = ['red', 'blue', 'orange', 'green', '_red', 'pink']
bar_colors = ['tab:red', 'tab:blue', 'tab:orange', 'tab:green', 'tab:red', 'tab:pink']

ax.bar(nomes, idades, label=bar_labels, color=bar_colors)

ax.set_ylabel('Nomes')
ax.set_title('Nomes e idades')
ax.legend(title='Nomes idades coloridas')

plt.show()
"""