class ProductsRepository:
  def __init__(self, connection) -> None:
    self.__connection = connection
  
  def find_product_by_name(self, product_name: str) -> tuple:
    cursor = self.__connection.cursor()
    cursor.execute("SELECT * FROM products WHERE name = ?", (product_name,))
    product = cursor.fetchone()
    return product
  
  def insert_product(self, name: str, price: float, quantity: int) -> None:
    cursor = self.__connection.cursor()
    cursor.execute("INSERT INTO products (name, price, quantity) VALUES (?, ?, ?)",
                   (name, price, quantity,))
    self.__connection.commit()
    