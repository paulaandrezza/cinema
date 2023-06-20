from classeBase import ClasseBase


class Sala(ClasseBase):
  def __init__(self, conn):
    super().__init__(conn)

  def inserir_unitario(self, params, values):
    try:
      for param, value in zip(params, values):
        if param == 'qtdAssentos':
          try:
            value = int(value)
          except ValueError:
            raise ValueError("Formato inválido para a quantidade de assentos. Insira somente inteiros!")
        elif param == 'idUnidade':
          tabela = 'UNIDADE'
          exists = self.consultar_foreignKey(tabela, param, value)
          if exists[0] == 0:
            raise ValueError("Esse id não existe em Unidade. Insira somente ids válidos!")
      
      return self.inserir('SALA', params, values)
    except ValueError as e:
      print(f"\033[0;30;41m\nErro: {str(e)}\033[m")
      input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
      return
    
  def atualizar_coluna(self, values):
    return self.atualizar('SALA', values[0], values[2], f"idSala = {values[1]}")
  
  def consultar_todos(self):
    join_clauses = [
      "UNIDADE ON SALA.idUnidade = UNIDADE.idUnidade"
    ]
    resultado = self.consultar('SALA', join_clauses)
    if resultado:
      print("{:<3} {:<15} {:<15} {:<30} {:<30} {:<30} {:<40} {:<3}".format("ID", "Qtd Assentos", "Id Unidade", "Estado", "Cidade", "Bairro", "Logradouro", "Número"))
      for item in range(len(resultado)):
        print("{:<3} {:<15} {:<15} {:<30} {:<30} {:<30} {:<40} {:<3}".format(resultado[item][0], resultado[item][1], resultado[item][2], resultado[item][4], resultado[item][5], resultado[item][6],  resultado[item][7], resultado[item][8]))
    input("\033[1;44m\nPressione <ENTER> para continuar...\033[m")
    return

  def excluir_unitario(self, id_sala):
    return self.excluir('SALA', f"idSala = {id_sala}")

