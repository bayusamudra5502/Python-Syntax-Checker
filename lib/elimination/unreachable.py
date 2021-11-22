"""Module recheable
Melakukan eliminasi simbol-simbol yang unreachable dari start point
"""

from lib.elimination import Elimination
from lib.cfg import CFG
from util.boolmatrix import BoolMatrix

class UnreachableElimination(Elimination):
  def __init__(self, cfg: CFG) -> None:
    super().__init__(cfg)
    self.__label = tuple(cfg.rules.keys())
    self.__lastTerminal = set()
    self.__lastTerminal = self.__lastTerminal.union(cfg.groups.keys())
    self.__lastTerminal = self.__lastTerminal.union(cfg.terminals)
    
  def __buildReachableTable(self):
    """Membangun Tabel Reachable"""
    table = BoolMatrix(len(self.__label))

    for i in range(len(self.__label)):
      for j in super().rules[self.__label[i]]:
        for k in j:
          if k in self.__label:
            end = self.__label.index(k)
            table.matrix[i,end] = True
    
    self.__table = table
  
  def __symbolReachable(self, rule: tuple):
    """Mengembalikan True bila semua rule reachable"""
    for i in rule:
      if not i in self.__lastTerminal and not i in self.__reachable:
        return False
    
    return True
  
  def eliminate(self) -> CFG:
    """Menghilangkan semua unreachable symbol pada CFG."""
    
    self.__buildReachableTable()

    closure = self.__table.transitiveClosure()
    startIdx = self.__label.index(super().start)
    self.__reachable = []

    for j in range(len(self.__label)):
      if closure[startIdx, j]:
        self.__reachable.append(self.__label[j])
    
    result = {}
    newTerminal = set()

    for i in self.__reachable:
      # Menyaring rule hanya yang reachable
      result[i] = tuple(filter(lambda x: self.__symbolReachable(x), super().rules[i]))

      # Memasukan reachable terminal
      for j in result[i]:
        for k in j:
          if k in self.__lastTerminal:
            newTerminal.add(k)
      
    return CFG(result, super().groups, list(newTerminal), super().start)
