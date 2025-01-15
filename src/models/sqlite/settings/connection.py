import sqlite3 as sqlite
from sqlite3 import Connection as sqliteConnection

class sqliteConnectionHandle:
  def __init__(self) -> None:
    self.__connection_str = "storage.db"
    self.__connection = None
  
  def connect(self) -> sqliteConnection:
    connection = sqlite.connect(self.__connection_str, 
                                check_same_thread=False)
    self.__connection = connection
    return connection
  
  def get_connection(self) -> sqliteConnection:
    return self.__connection