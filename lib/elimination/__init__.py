"""
Module Elimination
Implementasi semua step eliminasi pada pembentukan CNF
"""

from abc import ABC, abstractmethod
from lib.cfg import CFG

class Elimination(ABC):
  """Abstract Class untuk Kelas Step Eliminasi"""
  def __init__(self, cfg: CFG) -> None:
      self.__rules = cfg
  
  @property
  def rules(self) -> dict:
    return self.__rules.rules
  
  @property
  def groups(self) -> dict:
    return self.__rules.groups

  @property
  def terminals(self) -> tuple:
    return self.__rules.terminals

  @abstractmethod
  def eliminate(self) -> CFG:
    pass
