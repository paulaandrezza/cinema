import datetime

from classeBase import ClasseBase


class Sessao(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    try:     
      for param, value in zip(params, values):
        if param == "horario":
          try:
            datetime.datetime.strptime(value, "%H:%M")
          except ValueError:
            raise ValueError("Formato inválido para o horário. Utilize o formato HH:MM.")
        elif param == "data":
          try:
            datetime.datetime.strptime(value, "%d/%m/%Y")
          except ValueError:
            raise ValueError("Formato inválido para a data. Utilize o formato DD/MM/YYYY.")
      
      return self.inserir('SESSAO', params, values)
    except ValueError as e:
      print(f"\033[0;30;41m\nErro: {str(e)}\033[m")
      input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
      return

  def atualizar_coluna(self, values):
    return self.atualizar('SESSAO', values[0], values[2], f"idSessao = {values[1]}")

  def consultar_todos(self):
    join_clauses = [
      "FILME ON FILME.idFilme = SESSAO.idFilme",
      "SALA ON SALA.idSala = SESSAO.idSala"
    ]
    resultado = self.consultar('SESSAO', join_clauses)
    if resultado:
      print("{:<3} {:<15} {:<15} {:<10} {:<15} {:<30} {:<50} {:<15} {:<15} {:<15} {:<15}".format("ID", "Horário", "Data", "idFilme", "idSala", "Nome", "Descrição", "Genêro", "Duração (min)", "Classificação", "Qtd Assentos"))
      for item in range(len(resultado)):
        print("{:<3} {:<15} {:<15} {:<10} {:<15} {:<30} {:<50} {:<15} {:<15} {:<15} {:<15}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][3], resultado[item][4], resultado[item][6], resultado[item][7], resultado[item][8], resultado[item][9], resultado[item][10], resultado[item][12]))
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_sessao):
    return self.excluir('SESSAO', f"idSessao = {id_sessao}")

