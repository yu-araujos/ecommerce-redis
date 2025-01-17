from abc import ABC, abstractmethod

class RedisRepositoryInterface(ABC):

  @abstractmethod
  def set_key(self, key: str, value: any) -> None: pass
    
  @abstractmethod
  def get_key(self, key: str) -> str: pass

  @abstractmethod
  def set_hash(self, key: str, field: str, value: any) -> None: pass
    
  @abstractmethod
  def get_hash(self, key: str, field: str) -> any: pass

  @abstractmethod
  def set_expiring(self, key: str, value: any, expiring: int) -> None: pass
    
  @abstractmethod
  def set_hash_exp(self, key: str, field: str, value: any, expiring: int) -> None: pass
