"""Modul useless
Modul yang berisi implementasi useless symbol pada CFG
"""

from lib.elimination import Elimination
from lib.elimination.unreachable import UnreachableElimination
from lib.elimination.ungenerating import UngeneratingElimination
from lib.cfg import CFG

class UselessElimination(Elimination):
  def __init__(self, cfg: CFG) -> None:
    super().__init__(cfg)
    self.__cfg = cfg

  def eliminate(self) -> CFG:
    """
    Menghilangkan semua symbol yang useless

    Mengembalikan rule CFG yang useful
    """
    
    ue = UnreachableElimination(self.__cfg)
    return UngeneratingElimination(ue.eliminate()).eliminate()
    