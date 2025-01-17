import pytest
from src.models.sqlite.settings.connection import sqliteConnectionHandle
from src.models.sqlite.repository.products_repo import ProductsRepository

connection_handle = sqliteConnectionHandle()
connection = connection_handle.connect()

@pytest.mark.skip(reason="Interaction with BD test")
def test_insert_products():
    repo = ProductsRepository(connection)
    name = "Product 2"
    price = 10.0
    quantity = 10

    repo.insert_product(name, price, quantity)
    
@pytest.mark.skip(reason="Interaction with BD test")
def test_find_product_by_name():
    repo = ProductsRepository(connection)
    name = "Product 2"

    product = repo.find_product_by_name(name)
    print(product)
    print(type(product))