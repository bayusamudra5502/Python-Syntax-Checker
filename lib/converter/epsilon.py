from lib.converter.elimination import Elimination
from lib.cfg import CFG

class EpsilonElimination(Elimination):
  def __init__(self, cfg: CFG) -> None:
    super().__init__(cfg)
  
  def eliminate(self) -> CFG:
    result = self.__cfg
    return None