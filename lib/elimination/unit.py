"""
Modul unit
Modul ini merupakan implementasi dari Unit Production Elimination
"""

from lib.elimination import Elimination
from lib.cfg import CFG
from util.boolmatrix import BoolMatrix

class UnitElimination(Elimination):
  """Kelas pengeliminasi unit production"""
  def __init__(self, cfg: CFG) -> None:
    super().__init__(cfg)

  def __isUnitProd(self, test: tuple):
    """Mengembalikan true bila test merupakan Variabel"""
    if len(test) > 1:
      return False
    else:
      return test[0] in super().rules.keys()
    
  def __buildCookbook(self):
    """Membentuk rules tanpa adanya unit production"""
    self.__cookbook = {}

    for i in super().rules:
      self.__cookbook[i] = set(filter(lambda x: not self.__isUnitProd(x), super().rules[i]))
  
  def __buildBoolMatrix(self):
    """Membentuk matriks boolean untuk keterhubungan"""
    self.__label = tuple(super().rules.keys())

    unit = {}
    for i in super().rules:
      unit[i] = tuple(filter(lambda x: self.__isUnitProd(x), super().rules[i]))
    
    self.__matrix = BoolMatrix(len(self.__label))

    for i in range(len(self.__label)):
      for j in unit[self.__label[i]]:
        idx = self.__label.index(j[0])
        self.__matrix.matrix[i,idx] = True

  
  def eliminate(self) -> CFG:
    """Melakukan eliminasi unit production pada CFG"""
    self.__buildCookbook()
    self.__buildBoolMatrix()

    closure = self.__matrix.transitiveClosure()
    newRules = {}

    for i in range(len(self.__label)):
      newRule = set()

      for j in range(len(self.__label)):
        if closure[i,j]:
          newRule = newRule.union(self.__cookbook[self.__label[j]])
      
      newRules[self.__label[i]] = tuple(newRule)
    
    return CFG(newRules, super().groups, list(super().terminals), super().start)
