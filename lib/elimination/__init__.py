"""
Module Elimination
Implementasi semua step eliminasi pada pembentukan CNF
"""

from abc import ABC, abstractmethod
from lib.cfg import CFG

class Elimination(ABC):
  """Abstract Class untuk Kelas Step Eliminasi"""
  def __init__(self, cfg: CFG) -> None:
      self.__cfg = cfg
  
  @abstractmethod
  def eliminate(self) -> CFG:
    pass
