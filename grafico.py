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
