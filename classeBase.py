class Base:
  def __ini__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()

  # INSERIR
  def inserir(self, )