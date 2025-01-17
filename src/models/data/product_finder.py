from src.models.sqlite.repository.interfaces.products_repo import ProductsRepositoryInterface
from src.models.redis.repository.interfaces.redis_repo import RedisRepositoryInterface

class ProductFinder:
  def __init__(self, redis_repo: RedisRepositoryInterface, 
               products_repo: ProductsRepositoryInterface) -> None:
    self.__redis_repo = redis_repo
    self.__products_repo = products_repo
    