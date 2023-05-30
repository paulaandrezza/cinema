class Filme:
  def __init__(self, conn):
    self.conn = conn
    self.cursor = self.conn.cursor()
    