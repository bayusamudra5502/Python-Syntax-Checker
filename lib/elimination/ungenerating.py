"""Modul generating
Implementasi dari pengeliminasi symbol yang tidak generating.
"""

from lib.elimination import Elimination
from lib.cfg import CFG

class UngeneratingElimination(Elimination):
  """Kelas pengeliminasi ungenerating symbol"""

  def  __init__(self, cfg: CFG) -> None:
    super().__init__(cfg)
    self.__terminal = set()
    self.__generating = set()
    self.__buildTerminalTable()

  def __buildTerminalTable(self):
    """Membentuk tabel terminal"""
    self.__terminal = self.__terminal.union(super().terminals)
    self.__terminal = self.__terminal.union(super().groups.keys())

  def isGenerating(self, rule: tuple) -> bool:
    """Mengembalikan true bila rule generating berdasarkan
    terminal table dan generating table saat ini"""
    for i in rule:
      if (not i in self.__terminal and not i in self.__generating):
        return False
    
    return True

  def eliminate(self) -> CFG:
    """Melakukan eliminasi ungenerating symbol.
    
    Mengembalikan CFG yang semua symbolnya generating
    """
    
    generatingRule = {}
    isChanged = True

    while(isChanged):
      isChanged = False

      for i in super().rules:
        for j in super().rules[i]:
          if(self.isGenerating(j)):
            if((i in generatingRule and not j in generatingRule[i]) 
                or (not i in generatingRule)):
              # Ditemukan rule yang generating dan belum terdaftar
              isChanged = True
              
              # Update data generating rule
              if i in generatingRule:
                generatingRule[i].add(j)
              else:
                generatingRule[i] = set()
                generatingRule[i].add(j)
              
              # Update generating symbol table
              self.__generating.add(i)
    
    result = {}
    for i in generatingRule:
      result[i] = tuple(generatingRule[i])

    return CFG(result, super().groups, list(super().terminals), super().start)
    