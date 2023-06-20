from classeBase import ClasseBase


class Filme(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    try:
      for param, value in zip(params, values):
        if param == 'duracao':
          try:
            value = int(value)
          except ValueError:
            raise ValueError("Formato inválido para a duração. Insira somente inteiros!")
      
      return self.inserir('FILME', params, values)
    except ValueError as e:
      print(f"\033[0;30;41m\nErro: {str(e)}\033[m")
      input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
      return

  def atualizar_coluna(self, values):
    return self.atualizar('FILME', values[0], values[2], f"idFilme = {values[1]}")

  def consultar_todos(self):
    resultado = self.consultar('FILME')
    if resultado:
      print("{:<3} {:<30} {:<50} {:<15} {:<15} {:<15}".format("ID", "Nome", "Descrição", "Genêro", "Duração (min)", "Classificação"))
      for item in range(len(resultado)):
        print("{:<3} {:<30} {:<50} {:<15} {:<15} {:<15}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][5]))
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_filme):
    return self.excluir('FILME', f"idFilme = {id_filme}")


# Exemplo de uso:
# conn = # Conexão com o banco de dados

# filme = Filme(conn)
# filme.inserir_filme((1, 'Filme 1', 'Descrição 1', 'Ação', 120, 14))
# filme.atualizar_coluna(('descricao', 1, 'Nova descrição'))
# filme.consultar_filmes()
# filme.excluir_filme(1)
