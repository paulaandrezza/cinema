from classeBase import ClasseBase

class Filme(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_filme(self, params, values):
    return self.inserir('FILME', params, values)

  def atualizar_descricao(self, filme):
    return self.atualizar('FILME', 'descricao', filme[1], f"idFilme = {filme[0]}")

  def consultar_filmes(self):
    return self.consultar('FILME')

  def excluir_filme(self, id_filme):
    return self.excluir('FILME', f"idFilme = {id_filme}")


# Exemplo de uso:
# conn = # Conexão com o banco de dados

# filme = Filme(conn)
# filme.inserir_filme((1, 'Filme 1', 'Descrição 1', 'Ação', 120, 14))
# filme.atualizar_descricao((1, 'Nova descrição'))
# filme.consultar_filmes()
# filme.excluir_filme(1)
