from abc import ABC, abstractmethod
from lib.cfg import CFG

class Elimination(ABC):
  def __init__(self, cfg: CFG) -> None:
      self.__cfg = cfg
  
  @abstractmethod
  def eliminate(self) -> CFG:
    pass
