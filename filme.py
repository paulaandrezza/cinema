from classeBase import ClasseBase


class Filme(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_filme(self, values):
    params = ['nome', 'descricao', 'genero', 'duracao', 'classificacao']
    return self.inserir('FILME', params, values)

  def atualizar_coluna(self, filme):
    return self.atualizar('FILME', filme[0], filme[2], f"idFilme = {filme[1]}")

  def consultar_filmes(self):
    resultado = self.consultar('FILME')
    if resultado:
      print("{:<3} {:<30} {:<50} {:<15} {:<15} {:<3}".format("ID", "Nome", "Descrição", "Genêro", "Duração (min)", "Classificação"))
      for item in range(len(resultado)):
        print("{:<3} {:<30} {:<50} {:<15} {:<15} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5]))
    input("\033[1;44mPressione <ENTER> para continuar...\033[m")
    return

  def excluir_filme(self, id_filme):
    return self.excluir('FILME', f"idFilme = {id_filme}")


# Exemplo de uso:
# conn = # Conexão com o banco de dados

# filme = Filme(conn)
# filme.inserir_filme((1, 'Filme 1', 'Descrição 1', 'Ação', 120, 14))
# filme.atualizar_coluna(('descricao', 1, 'Nova descrição'))
# filme.consultar_filmes()
# filme.excluir_filme(1)
