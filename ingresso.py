from classeBase import ClasseBase


class Ingresso(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    try:
      for param, value in zip(params, values):
        if param == 'idSessao':
          tabela = 'SESSAO'
          exists = self.consultar_foreignKey(tabela, param, value)
          if exists[0] == 0:
            raise ValueError("Esse id não existe em Sessão. Insira somente ids válidos!")
      
      return self.inserir('INGRESSO', params, values)
    except ValueError as e:
      print(f"\033[0;30;41m\nErro: {str(e)}\033[m")
      input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
      return    

  def atualizar_coluna(self, values):
    return self.atualizar('INGRESSO', values[0], values[2], f"idIngresso = {values[1]}")

  def consultar_todos(self):
    join_clauses = [
      "SESSAO ON INGRESSO.idSessao = SESSAO.idSessao",
      "FILME ON SESSAO.idFilme = FILME.idFilme"
    ]
    resultado = self.consultar('INGRESSO', join_clauses)
    if resultado:
      print("{:<3} {:<30} {:<10} {:<10} {:<15} {:<10} {:<30} {:<40} {:<15}".format("ID", "Nome do Cliente", "Id Sessão", "Horário", "Data", "idSala", "Nome Filme", "Descrição", "Gênero"))
      for item in range(len(resultado)):
        print("{:<3} {:<30} {:<10} {:<10} {:<15} {:<10} {:<30} {:<40} {:<15}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][4], resultado[item][5],  resultado[item][7], resultado[item][9], resultado[item][10], resultado[item][11]))
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_ingresso):
    return self.excluir('INGRESSO', f"idIngresso = {id_ingresso}")

