from redis import Redis
from interfaces.redis_repository import RedisRepositoryInterface

class RedisRepository(RedisRepositoryInterface):
  def __init__(self, redis_conn: Redis) -> None:
    self.redis_conn = redis_conn
    
  def set_key(self, key: str, value: any) -> None:
    self.redis_conn.set(key, value)
    
  def get_key(self, key: str) -> str:
    value = self.__redis_conn.get(key)
    
    if value:
      rerturn value.decode('utf-8')
    return None
  
  def set_hash(self, key: str, field: str, value: any) -> None:
    self.__redis_conn.hset(key, field, value)
    
  def get_hash(self, key: str, field: str) -> any:
    value = self.__redis_conn.hget(key, field)
    
    if value:
      return value.decode('utf-8')
    return None
  
  def set_expiring(self, key: str, value: any, expiring: int) -> None:
    self.__redis_conn.set(key, value, expiring)
    
  def set_hash_exp(self, key: str, field: str, value: any, expiring: int) -> None:
    self.__redis_conn.hset(key, field, value)
    self.__redis_conn.expire(key, expiring)